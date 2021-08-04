from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name


class Product(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=False)
    content = models.TextField(max_length=500, blank=False)
    price = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='%Y/%m/%d/')


class Chefs(models.Model):
    chef_name = models.CharField(max_length=50, blank=False)
    chef_photo = models.ImageField(upload_to='chefs/')
    chef_profession = models.CharField(max_length=50, blank=False)


class Contact(models.Model):
    name = models.TextField(max_length=100)
    email = models.EmailField()
    phone = models.PositiveIntegerField()
    number_guests = models.PositiveIntegerField()
    date_reservation = models.DateTimeField(auto_now_add=False)
    time = models.CharField(max_length=50)
    message = models.TextField(max_length=5000)
