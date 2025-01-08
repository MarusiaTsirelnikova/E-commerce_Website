from django.urls import path
from .views import cart_add, cart_detail, remove_from_cart, delete_from_cart, append_to_cart


app_name = 'Cart'

urlpatterns = [
    path('add/<int:product_id>', cart_add, name='cart_add'),
    path('append/<int:product_id>', append_to_cart, name='cart_append'),
    path('delete/<int:product_id>', delete_from_cart, name='cart_delete'),
    path('remove/<int:product_id>/', remove_from_cart, name='remove'),
    path('', cart_detail, name='cart_detail'),
]
