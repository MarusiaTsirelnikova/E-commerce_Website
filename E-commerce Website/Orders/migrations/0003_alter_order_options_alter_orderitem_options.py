# Generated by Django 5.1.4 on 2025-01-08 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Orders', '0002_alter_order_address_alter_order_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'verbose_name': 'Заказ', 'verbose_name_plural': 'Заказы'},
        ),
        migrations.AlterModelOptions(
            name='orderitem',
            options={'verbose_name': 'Детали заказа', 'verbose_name_plural': 'Детали заказов'},
        ),
    ]
