from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Supplier(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=255)
    email = models.EmailField()


class Article(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    serial_number = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    image = models.ImageField(upload_to='articles/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    reception_date = models.DateField()


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
