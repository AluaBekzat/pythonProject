from django.contrib import admin

# Register your models here.
from product_list.models import Product, Category

admin.site.register(Product)
admin.site.register(Category)

from product_list.models import Genre, Book

admin.site.register(Book)
admin.site.register(Genre)