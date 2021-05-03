from django.shortcuts import HttpResponse
from product_analytics.utils import dashboard_report, revenue_by_brands, count_currently_and_previous_date, \
    count_revenue_by_type_clients
from product_analytics.cohorts import cohorts
from datetime import date


# Create your views here.
def dashboard(request):
    dates = count_currently_and_previous_date(date.today(), 'month')
    revenue_brands = revenue_by_brands(dates.get('currently_start'), dates.get('currently_end'))
    revenue, clients, revenue_by_type_clients = dashboard_report(date.today(), 'month')
    cohort = cohorts()
    html = "<html><body>%s</body></html>" % revenue, revenue_by_type_clients, clients, revenue_brands, cohort
    return HttpResponse(html)

