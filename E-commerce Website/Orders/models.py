from django.db import models
from Catalog.models import Product

# Create your models here.


class Order(models.Model):
    customer_name = models.CharField(verbose_name="Получатель", max_length=150)
    email = models.EmailField()
    address = models.CharField(verbose_name="Адрес доставки", max_length=250)
    created_at = models.DateTimeField(verbose_name="Создано", auto_now_add=True)
    paid = models.BooleanField(verbose_name="Статус оплаты", default=False)

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class OrderItem(models.Model):
    order = models.ForeignKey(Order, verbose_name="Заказ",  related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Продукт",  related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name="Цена за единицу",  max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(verbose_name="Количество", default=1)

    def get_cost(self):
        return self.price * self.quantity

    class Meta:
        verbose_name = 'Детали заказа'
        verbose_name_plural = 'Детали заказов'
