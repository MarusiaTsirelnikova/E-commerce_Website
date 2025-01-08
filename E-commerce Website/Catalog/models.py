from django.db import models
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(verbose_name="Название категории", max_length=100)
    slug = models.SlugField(verbose_name="Slug", unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class PlantCategory(models.Model):
    name = models.CharField(verbose_name="Название категории растения", max_length=100)
    slug = models.SlugField(verbose_name="Slug", unique=True)

    class Meta:
        verbose_name = 'Категория растений'
        verbose_name_plural = 'Категории растений'

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория товара", related_name='products', on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название товара", max_length=100)
    slug = models.SlugField(verbose_name="Slug", unique=True)
    description = models.TextField(verbose_name="Описание товара", max_length=750)
    plant_name = models.CharField(verbose_name="Имя растения", max_length=30, blank=True)
    plant_category = models.ForeignKey(PlantCategory, verbose_name="Категория растения", related_name='products', on_delete=models.CASCADE, blank=True)
    price = models.DecimalField(verbose_name="Цена товара", max_digits=8, decimal_places=2)
    available = models.BooleanField(verbose_name="Доступно к продаже", default=True)
    main_image = models.ImageField(verbose_name="Главное изображение", upload_to='products/', blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'category': self.category.slug, 'id': self.id, 'slug': self.slug, 'plant_category': self.plant_category.slug})
