from django.db import models



class  Genre1(models.Model):
    genre = models.CharField(max_length=50)

    def __str__(self):
        return self.genre

class Book1(models.Model):
    name = models.CharField(max_length=30)
    info = models.TextField()
    genre = models.ForeignKey(Genre1, null=True, blank=True, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.name} - {self.genre}'