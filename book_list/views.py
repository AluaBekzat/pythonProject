from django.shortcuts import render

# Create your views here.
from product_list.models import Product, Category

def all_book(request):
    book = Product.objects.all()
    genre = Category.objects.all()
    context = {
        'book' : book,
        'genre' : genre
    }
    return render (request, 'main.html', context)