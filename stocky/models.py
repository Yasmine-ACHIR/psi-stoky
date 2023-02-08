from datetime import date

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    serial_number = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='images/articles/')
    categories = models.ManyToManyField(Category)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    reception_date = models.DateField(default=date.today)


class Stock(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    reception_date = models.DateField()
    command = models.TextField()


class Invoice(models.Model):
    date = models.DateField()
    articles = models.ManyToManyField(Article)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
