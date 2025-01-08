from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, PlantCategory, Product

# Create your views here.


def product_list(request, category_slug=None, plant_category_slug=None):
    category = ''
    plant_category = ''
    products = Product.objects.filter(available=True)
    categories = Category.objects.all()
    plant_categories = PlantCategory.objects.all()

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if plant_category_slug:
        plant_category = get_object_or_404(PlantCategory, slug=plant_category_slug)
        products = products.filter(plant_category=plant_category)

    return render(request, 'catalog.html', {
        'category': category,
        'plant_category': plant_category,
        'products': products,
        'categories': categories,
        'plant_categories': plant_categories,
    })


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, available=True)

    return render(request, 'product_detail.html', {
        'product': product,
    })
