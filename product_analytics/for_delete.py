from product_analytics.models import MarketOrdersProducts
from datetime import datetime, timedelta

first_date = datetime.strptime('01/01/20', '%d/%m/%y')
last_date = datetime.strptime('01/01/21', '%d/%m/%y')


# all_orders = MarketOrdersProducts.objects.filter(created_at__range=(first_date, last_date))
offline_orders = MarketOrdersProducts.objects.\
    values_list('orderid', 'productid', 'price', 'quantity', 'discount').\
    filter(orderid__status=4).filter(orderid__type=1)

online_orders = MarketOrdersProducts.objects.\
    values_list('orderid', 'productid', 'price', 'quantity', 'discount').\
    filter(orderid__status=4).filter(orderid__type=0)


offline_id = []
online_id =[]

[offline_id.append(i[0]) for i in offline_orders]
[online_id.append(i[0]) for i in online_orders]


summ_discount = 0
summ_value = 0
count = 0

for i in all_orders_test:
    discount = i[2] * i[3] * int(i[4])/100
    value = i[2] * i[3]
    summ_discount += discount
    summ_value += value
    count += 1

# statuses orders in market_orders
# 0 = online
# 1 = offline