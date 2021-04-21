from django.urls import path
from product_analytics import views

urlpatterns = [
    path('', views.dashboard),
    path('revenue/', views.table_brands_revenue)
]
