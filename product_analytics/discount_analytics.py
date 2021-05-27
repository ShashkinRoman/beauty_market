from product_analytics.models import MarketOrdersProducts, MarketOrders
from datetime import date
import pandas as pd
import numpy as np
from collections import Counter
from product_analytics.models import MarketProducts
from django.db.models import Count
import csv

"""
Получить список уникальных prouct_id по которым были акции, за период
Посмотреть для каждого product_id количество товаров в новых чеках(количесвто чеков) и в старых чеках
Посчитать средний чек для каждой акции
Посчитать стоимость акции (количество товаров умноженных на среднюю цену без акции минус цена по акции)
Объем выручки с акциями и без
Количесвто продаж с акцией и без
"""

"""
Получить все первые продажи с датами и orderID
Посчитать, сколько раз был каждый товар куплен со скидкой больше 10%
"""


def find_number_and_products_new_clients(start_date, end_date):
    orders = MarketOrders.objects.filter(created_at__range=(start_date, end_date)).values_list('orderid', 'phone',
                                                                                               'created_at', 'sum')
    df = pd.DataFrame(orders, columns=['orderid', 'phone', 'created_at', 'sum'])

    df['order_period'] = df.created_at.apply(lambda x: x.strftime('%Y-%m-%d'))
    # добавим индекс в dataFrame по phone
    df.set_index('phone', inplace=True)
    df['join_month'] = df.groupby(level=0)['created_at'].min().apply(lambda x: x.strftime('%Y-%m-%d'))
    # df.reset_index(inplace=True)

    df.sort_values('phone').groupby('join_month').first()

    only_new_orders = list(df.sort_values('phone').groupby('join_month').first().orderid)
    all_products_in_new_orders = MarketOrders.objects.filter(rn_product_in_orders__orderid__in=only_new_orders).\
        values_list('rn_product_in_orders__productid', flat=True)

    count_ = Counter(all_products_in_new_orders).most_common()
    return count_


def find_number_and_products_returness_clients(start_date, end_date):
    # orders = MarketOrders.objects.filter(created_at__range=(start_date, end_date)).values_list('orderid', 'phone',
    #                                                                                            'created_at', 'sum')
    # non_unique_import_phones = list(MarketOrders.objects.order_by('phone')
    #                                 .values_list('phone', flat=True)
    #                                 .annotate(phone_count=Count('phone'))
    #                                 .filter(phone_count__gt=1))
    #
    # orders = MarketOrders.objects.filter(created_at__range=(start_date, end_date)).\
    #     filter(phone__in=non_unique_import_phones).values_list('orderid', 'phone', 'created_at', 'sum')
    #
    # df = pd.DataFrame(orders, columns=['orderid', 'phone', 'created_at', 'sum'])
    #
    # df['order_period'] = df.created_at.apply(lambda x: x.strftime('%Y-%m-%d'))
    # # добавим индекс в dataFrame по phone
    # df.set_index('phone', inplace=True)
    # df['join_month'] = df.groupby(level=0)['created_at'].min().apply(lambda x: x.strftime('%Y-%m-%d'))
    # # df.reset_index(inplace=True)
    #
    # only_first = df.sort_values('phone').groupby('join_month').first()
    #
    # count_ = Counter(all_products_in_new_orders).most_common()

    all_products_in_new_orders = MarketOrders.objects.\
        values_list('rn_product_in_orders__productid', flat=True)

    count_ = Counter(all_products_in_new_orders).most_common()


    pass


# def write_csv(list_):
#     with open('rating_product.csv', 'a', newline="") as csv_file:
#         writer = csv.writer(csv_file)
#         writer.writerow(('id', 'name', 'quantity'))
#
#         for i in list_:
#             writer.writerow((i[0], i[1], i[2]))


def find_name_for_product_id(count_):
    products_id = []
    table = []
    for i in count_:
        products_id.append(i[0])
        table.append((i[0], i[1]))

    tuples_with_name = MarketProducts.objects.filter(productid__in=products_id).values_list('productid', 'name')

    lists_final = []
    for tup1, tup2 in zip(tuples_with_name, table):
        lists_final.append((tup1[0], tup1[1], tup2[1]))

    lists_final.sort(key=lambda x: x[2])
    return lists_final

#
# def get_info_about_discount(start_date: date, end_date: date):
#     all_product_id = MarketOrdersProducts.objects.filter(orderid__status=4). \
#         filter(created_at__range=(start_date, end_date)).filter(
#         productid__rn_market_products__productid__sale=1). \
#         values_list('price', 'quantity', 'discount')


def main():
    start_date = date(2021, 4, 1)
    end_date = date(2021, 5, 1)
    product_id = 12543

    count_ = find_number_and_products_new_clients(start_date, end_date)
    find_name_for_product_id(count_)


if __name__ == '__main__':
    main()
