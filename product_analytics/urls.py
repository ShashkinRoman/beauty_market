from django.urls import path
from product_analytics import views

urlpatterns = [
    path('analytics/', views.dashboard),
]
