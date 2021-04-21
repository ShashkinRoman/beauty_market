from django.shortcuts import render
from product_analytics.utils import dashboard_report
from datetime import date


# Create your views here.


def dashboard(request):
    currently_period_revenue, previous_period_revenue, \
    currently_active_clients, previous_active_clients = dashboard_report(date.today(), 'week')
    return render(request, 'dashboard.html', {'currently_online_revenue': '%.1f' % currently_period_revenue.get('online_revenue'),
                                              'currently_online_discount': '%.1f' % currently_period_revenue.get('online_discount'),
                                              'currently_offline_revenue': '%.1f' % currently_period_revenue.get('offline_revenue'),
                                              'currently_offline_discount': '%.1f' % currently_period_revenue.get('offline_discount'),

                                              'previous_online_revenue': '%.1f' % previous_period_revenue.get('online_revenue'),
                                              'previous_online_discount': '%.1f' % previous_period_revenue.get('online_discount'),
                                              'previous_offline_revenue': '%.1f' % previous_period_revenue.get('offline_revenue'),
                                              'previous_offline_discount': '%.1f' % previous_period_revenue.get('offline_discount'),

                                              'currently_all_clients': '%.1f' % currently_active_clients.get("all_clients"),
                                              'currently_new_clients': '%.1f' % currently_active_clients.get("new_clients"),
                                              'currently_returness_clients': '%.1f' % currently_active_clients.get("returness_clients"),

                                              'previous_all_clients': '%.1f' % previous_active_clients.get("all_clients"),
                                              'previous_new_clinets': '%.1f' % previous_active_clients.get("new_clients"),
                                              'previous_returness_clinets': '%.1f' % previous_active_clients.get("returness_clients")
                                              })
