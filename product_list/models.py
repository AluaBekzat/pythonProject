from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=50)

    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} - {self.category}'




