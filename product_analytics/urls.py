from django.urls import path
from product_analytics.views import DashboardView, dashboard
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='analytics'), name='name'),
    path('analytics/', DashboardView.as_view(), name='analytics_url'),
    path('analytics2/', dashboard)
]
