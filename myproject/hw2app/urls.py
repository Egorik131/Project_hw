from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_clients/', views.get_clients, name='get_client'),
    path('clients/<int:client_id>/', views.get_client_on_id, name='get_clients'),
    path('client_orders/<int:client_id>/', views.get_clients_orders, name='get_client_orders'),
    path('orders_date/<int:client_id>/<int:days>/', views.get_orders_on_date, name='get_orders_on_date'),
    path('add_product/', views.product_form, name='add_product'),
]