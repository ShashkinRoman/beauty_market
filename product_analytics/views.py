from django.shortcuts import HttpResponse, render
from product_analytics.utils import dashboard_report, revenue_by_brands, count_currently_and_previous_date, \
    count_revenue_by_type_clients, sending_by_city
from product_analytics.cohorts import cohorts
from datetime import date
from product_analytics.forms import DateForm
from django.views import View
from IPython.display import HTML
import json


# Create your views here.
def dashboard(request):
    dates = count_currently_and_previous_date(date.today(), 'month')
    revenue_brands = revenue_by_brands(dates.get('currently_start'), dates.get('currently_end'))
    revenue, clients, revenue_by_type_clients = dashboard_report(dates)

    cohort = cohorts()
    html = "<html><body>%s</body></html>" % revenue, revenue_by_type_clients, clients, revenue_brands, cohort
    return HttpResponse(html)


class DashboardView(View):
    def get(self, request):
        form = DateForm()
        dates = count_currently_and_previous_date(date.today(), 'month')
        revenue_brands = revenue_by_brands(dates.get('currently_start'), dates.get('currently_end'))
        revenue, clients, revenue_by_type_clients = dashboard_report(dates)
        data = json.loads(revenue)
        data_revenue_by_type_clients = json.loads(revenue_by_type_clients)
        data_clients = json.loads(clients)
        data_revenue_brands = json.loads(revenue_brands)
        sendings_by_city = sending_by_city(dates.get('currently_start'), dates.get('currently_end'))
        sendings_by_city_at_range = json.loads(sendings_by_city[0])
        sendings_by_city_all = json.loads(sendings_by_city[1])
        cohort = cohorts()
        # html = "<html><body>%s</body></html>" % revenue, revenue_by_type_clients, clients, revenue_brands, cohort
        return render(request, 'dashboard.html', context={'form': form,
                                                          'revenue': data,
                                                          'clients': data_clients,
                                                          'revenue_by_type_clients': data_revenue_by_type_clients,
                                                          'revenue_brands': data_revenue_brands,
                                                          'cohort': cohort,
                                                          'sendings_by_city_at_range': sendings_by_city_at_range,
                                                          'sendings_by_city_all': sendings_by_city_all,
                                                          })

    def post(self, request):
        bound_form = DateForm(request.POST)

        # if bound_form.is_valid():
        if bound_form.is_valid():
            dates = count_currently_and_previous_date(
                [bound_form.cleaned_data['start_date'],
                 bound_form.cleaned_data['end_date']], '')
            revenue_brands = revenue_by_brands(dates.get('currently_start'), dates.get('currently_end'))
            revenue, clients, revenue_by_type_clients = dashboard_report(dates)
            data = []
            data = json.loads(revenue)
            data_revenue_by_type_clients = json.loads(revenue_by_type_clients)
            data_clients = json.loads(clients)
            data_revenue_brands = json.loads(revenue_brands)
            cohort = cohorts()
            return render(request, 'dashboard.html', context={'form': DateForm(),
                                                              'revenue': data,
                                                              'clients': data_clients,
                                                              'revenue_by_type_clients': data_revenue_by_type_clients,
                                                              'revenue_brands': data_revenue_brands,
                                                              'cohort': cohort})

        # return HttpResponse(revenue, form)