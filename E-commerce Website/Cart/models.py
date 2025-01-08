from django.db import models
from Catalog.models import Product

# Create your models here.


class Cart(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    def get_total_price(self):
        return sum(cart_item.get_total_price() for cart_item in self.items.all())


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, verbose_name="Корзина",  related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Товар в корзине", related_name='cart_items', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def get_total_price(self):
        return self.product.price * self.quantity
