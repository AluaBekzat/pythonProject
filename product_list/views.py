from django.shortcuts import render

# Create your views here.
from product_list.models import Product, Category


def all_products(request):
    products = Product.objects.all()
    category = Category.objects.all()
    context = {
        'products' : products,
        'category' : category
    }
    return render (request, 'main.html', context)

def products_on_category(request, pk):
    products = Product.objects.filter(category = pk)
    context = {
        'products': products
    }
    return render(request, 'main.html', context)

def querty (request):
    return render(request, '123.html')