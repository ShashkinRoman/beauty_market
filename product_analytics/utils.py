from datetime import timedelta, date
from calendar import monthrange
from product_analytics.models import MarketOrdersProducts, MarketOrders
from django.db.models import Count
import pandas as pd


def count_currently_and_previous_date(currently_date: date, period: str):
    """
    count for currently and previous start an end dates for week, month, year
    :param currently_date: 2020-03-18
    :param period: 'week' or 'month' or 'year'
    :return: dict with dates
    """
    currently_start, previous_start, previous_end = 0, 0, 0

    if period == 'week':
        currently_start = currently_date - timedelta(days=currently_date.weekday())
        previous_start = currently_start - timedelta(weeks=1)
        previous_end = currently_date - timedelta(weeks=1)

    if period == 'month':
        currently_start = date(currently_date.year, currently_date.month, 1)
        previous_start = date(currently_date.year, int(currently_date.month) - 1, 1)
        previous_end = date(currently_date.year, int(currently_date.month) - 1, currently_date.today().day
                            or monthrange(currently_date.year, int(currently_date.month - 1))[1])

    if period == 'year':
        currently_start = date(currently_date.year, 1, 1)
        previous_start = date(int(currently_date.year) - 1, 1, 1)
        previous_end = date(int(currently_date.year) - 1, currently_date.month, currently_date.day)

    return {'currently_start': currently_start,
            'currently_end': currently_date,
            'previous_start': previous_start,
            'previous_end': previous_end
            }


def count_revenue_for_period(start_date: date,
                             end_date: date,
                             # store: str,
                             ):
    """
    count offline and online revenue

    :param start_date: date(2021, 3, 15)
    :param end_date: date(2021, 3, 18)
    # :param store: 'moscow', 'saratov', 'balakovo', 'internet', 'all'
    :return:  inr revenue 245673,23
    """
    offline_orders = MarketOrdersProducts.objects. \
        values_list('orderid', 'productid', 'price', 'quantity', 'discount'). \
        filter(orderid__status=4).filter(orderid__type=1).filter(created_at__range=(start_date, end_date))

    online_orders = MarketOrdersProducts.objects. \
        values_list('orderid', 'productid', 'price', 'quantity', 'discount'). \
        filter(orderid__status=4).filter(orderid__type=0).filter(created_at__range=(start_date, end_date))

    online_revenue, online_discount = count_revenue(online_orders)
    offline_revenue, offline_discount = count_revenue(offline_orders)
    return {'online_revenue': online_revenue,
            'online_discount': online_discount,
            'offline_revenue': offline_revenue,
            'offline_discount': offline_discount
            }


def count_revenue(info_about_orders):
    revenue_value = 0
    discount_value = 0

    for i in info_about_orders:
        discount = i[2] * i[3] * int(i[4]) / 100
        value = i[2] * i[3]
        discount_value += discount
        revenue_value += value
    revenue = revenue_value - discount_value
    return revenue, discount_value


def count_active_clients_for_period(start_date: date, end_date: date,):
    """
    count active clients: all, new, returnees
    :param start_date: 2020-03-15
    :param end_date: 2020-03-18
    :return:
    """
    set_all_orders = list(set(MarketOrders.objects.values_list('phone', flat=True).
                              filter(created_at__range=(start_date, end_date))))
    all_orders = len(set_all_orders)
    non_unique_phones = list(MarketOrders.objects.order_by('phone')
                             .values_list('phone', flat=True)
                             .annotate(import_phone_count=Count('phone'))
                             .filter(import_phone_count__gt=1))
    for i in set_all_orders:
        if i in non_unique_phones:
            set_all_orders.remove(i)

    return {'all_clients': all_orders,
            'new_clients': len(set_all_orders),
            'returness_clients': all_orders - len(set_all_orders)
            }


def revenue_by_brands(start_date: date, end_date: date):
    """
    count revenue for every brands ad return dataframe adapted for html
    :param start_date: date
    :param end_date: date
    :return: DataFrame('brand', 'final_price')
    """
    orders = MarketOrdersProducts.objects.filter(
        productid__marketgroupid__rn_market_product_parameters__name="Бренд").filter(orderid__status=4).filter(
        created_at__range=(start_date, end_date)). \
        values_list('orderid', 'productid', 'price', 'quantity', 'discount',
                    'productid__marketgroupid__rn_market_product_parameters__name',
                    'productid__marketgroupid__rn_market_product_parameters__value')
    if len(orders) == 0:
        return pd.DataFrame(columns=['brand', 'final_price']).to_html()
    else:
        df = pd.DataFrame(orders, columns=['orderid', 'productid', 'price', 'quantity', 'discount', 'name_brand', 'brand'])
        df['discount'] = pd.to_numeric(df['discount'])
        df['brand'] = df['brand'].str.strip()
        df['brand'] = df['brand'].str.lower()
        df['brand'] = df['brand'].str.replace(' ', '')
        df['final_price'] = df.apply(lambda row: row.price * row.quantity * (100 - row.discount), axis=1)
        brends_revenue = df.drop_duplicates(subset=['brand'])[['brand', 'final_price']].sort_values('final_price', ascending=False)
        return brends_revenue.to_html()


def count_revenue_by_type_clients(start_date: date, end_date: date):
    """count revenue by new and returning clients"""
    currently_month = start_date.strftime('%Y-%m')
    all_orders = MarketOrders.objects.filter(status=4).\
        filter(deleted_at__isnull=True).values_list('orderid', 'phone', 'sum', 'created_at')

    df = pd.DataFrame(all_orders, columns=['orderid', 'phone', 'sum', 'created_at'])
    df['join_month'] = df.created_at.apply(lambda x: x.strftime('%Y-%m'))
    df.set_index('phone', inplace=True)
    df['join_month'] = df.groupby(level=0)['created_at'].min().apply(lambda x:x.strftime('%Y-%m'))
    df.astype({'sum': 'float'})

    revenue_by_new_clients = df.loc[df['join_month'] == currently_month]['sum'].sum()
    df['created_at'] = pd.to_datetime(df['created_at'])
    mask = (df['created_at'] > str(start_date)) & (df['created_at'] <= str(end_date))
    revenue_by_returning_clients = df.loc[mask & (df['join_month'] != currently_month)].sum()
    return {'revenue_by_new_clients': float(revenue_by_new_clients),
            'revenue_by_returning_clients': float(revenue_by_returning_clients['sum'])}


def dashboard_report(start_date, period):
    dates = count_currently_and_previous_date(start_date, period)
    # currently_period_revenue = count_revenue_for_period(dates.get('currently_start'), dates.get('currently_end'))
    # previous_period_revenue = count_revenue_for_period(dates.get('previous_start'), dates.get('previous_end'))
    # currently_active_clients = count_active_clients_for_period(dates.get('currently_start'), dates.get('currently_end'))
    # previous_active_clients = count_active_clients_for_period(dates.get('previous_start'), dates.get('previous_end'))
    df_revenue = pd.DataFrame([count_revenue_for_period(dates.get('currently_start'), dates.get('currently_end')),
                       count_revenue_for_period(dates.get('previous_start'), dates.get('previous_end'))],
                      index=['Текущий', 'Предыдущий'])
    df_clients = pd.DataFrame([count_active_clients_for_period(dates.get('currently_start'), dates.get('currently_end')),
                               count_active_clients_for_period(dates.get('previous_start'), dates.get('previous_end'))],
                               index=['Текущий', 'Предыдущий'])
    df_revenue_by_type_clients = pd.DataFrame([count_revenue_by_type_clients(dates.get('currently_start'), dates.get('currently_end')),
                                               count_revenue_by_type_clients(dates.get('previous_start'),
                                                                               dates.get('previous_end'))],
                                              index=['Выручка текущий период', 'Выручка предыдущий период'])
    return df_revenue.to_html(float_format=lambda x: '%10.2f' % x), \
           df_clients.to_html(float_format=lambda x: '%10.2f' % x), \
           df_revenue_by_type_clients.to_html(float_format=lambda x: '%10.2f' % x)


        # currently_period_revenue, previous_period_revenue, currently_active_clients, previous_active_clients


# def main():
#     start_date = date.today()
#     period = 'week'
start_date = date(2021, 4, 1)
end_date = date(2021, 5, 1)
    #
    # dashboard_report(start_date, period)
    # pass
#
#
# if __name__ == '__main__':
#     main()
