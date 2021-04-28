import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt
import matplotlib as mpl
from datetime import date
from product_analytics.models import MarketOrders


# import seaborn as sns


def cohort_period(df):
    df['cohort_period'] = np.arange(len(df)) + 1  # отсчет с 1
    return df


def cohorts():
    pd.set_option('max_columns', 500)
    mpl.rcParams['lines.linewidth'] = 500

    start_date = date(2019, 1, 1)
    end_date = date.today()
    orders = MarketOrders.objects.filter(created_at__range=(start_date, end_date)).values_list('phone', 'created_at',
                                                                                               'sum')

    df = pd.DataFrame(orders, columns=['phone', 'created_at', 'sum'])
    # определим когда была совершена покупка и добавим в order_period
    df['order_period'] = df.created_at.apply(lambda x: x.strftime('%Y-%m'))
    # добавим индекс в dataFrame по phone
    df.set_index('phone', inplace=True)
    # добавим столбец JoinMonth,  с датой первой покупки
    df['join_month'] = df.groupby(level=0)['created_at'].min().apply(lambda x: x.strftime('%Y-%m'))
    df.reset_index(inplace=True)
    # столбец в котором далее поместим количество заказов
    df.insert(len(df.columns), "total_orders", 0, allow_duplicates=False)
    grouped = df.groupby(['join_month', 'order_period'])
    # количество уникальных пользователей и общее количество заказов и выручка за период
    cohorts = grouped.agg({'phone': pd.Series.nunique,
                           'total_orders': pd.Series.count,
                           'sum': np.sum})
    # переименуем  столбцы для  наглядности
    cohorts.rename(columns={'phone': 'total_users',
                            'total_orders': 'total_orders'}, inplace=True)

    cohort_group_size = cohorts['total_users'].groupby(level=1).first()
    # добавление порядкового номера периода в cohort_period
    cohorts = cohorts.groupby(level=0).apply(cohort_period)

    # переиндексируем DataFrame
    cohorts.reset_index(inplace=True)
    cohorts.set_index(['cohort_period', 'join_month'], inplace=True)
    # создадим ряд содержаший размер каждой когорты JoinMonth
    cohort_group_size = cohorts['total_users'].groupby(level=1).first()
    # cohorts['total_users'].unstack(1).head(15)

    # users in percent
    user_retention = cohorts['total_users'].unstack(1).divide(cohort_group_size, axis=1)
    # user_retention.head()

    # revenue
    revenue_cohort = cohorts['sum'].unstack(1)

    #reset index cohort and visualisate
    #
    # cohorts.reset_index(inplace=True)
    # cohorts.set_index(['join_month', 'cohort_period'], inplace=True)
    #
    # cohort_group_size = cohorts['total_users'].groupby(level=0).first()
    # cohorts['total_users'].unstack(0)
    # user_retention = cohorts['total_users'].unstack(0).divide(cohort_group_size, axis=1)
    #
    #
    #
    # sns.set(style='ticks')
    # plt.figure(figsize=(24, 16))
    # plt.title('Cohorts: User Retention')
    # sns.heatmap(user_retention.T, mask=user_retention.T.isnull(), annot=True, fmt='.0%');
    df = cohorts['total_users'].unstack(1).head(50)
    return user_retention.transpose().to_html()

# def main():
#     start_date = date(2021, 3, 1)
#     end_date = date(2021, 4, 1)
#     cohorts()
