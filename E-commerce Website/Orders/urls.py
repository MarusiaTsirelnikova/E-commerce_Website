from django.urls import path
from . import views


app_name = 'Orders'

urlpatterns = [
    path('create', views.create_order, name='order_create'),
    path('confirmation/<int:order_id>', views.confirmation, name='confirmation'),
]
