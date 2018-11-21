from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

YESNO = (
    (1, 'yes'),
    (2,'no'),
)


class Koop(models.Model):
    name = models.CharField(max_length=255)
    #logo = models.ImageField(max_length=225, null=True)
    city = models.CharField(max_length=225)
    district = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=225)
    phone = models.CharField(max_length = 63, null=True, blank=True)

    def __str__(self):
        return self.name


class MyUser(AbstractUser):
    #phone = models.CharField(max_length = 63, null=True)
    #nickname = models.CharField(max_length=255)
    #email = models.CharField(max_length=255, primary_key=True)
    #password = models.CharField(max_length=255)
    #photo = models.ImageField(max_length=225, null=True)
    #kooperatywa = models.CharField(max_length=255, null=True)
    #supplier = models.IntegerField(choices=YESNO, )
    #koopadmin = models.IntegerField(choices=YESNO)
    koop = models.ForeignKey(Koop, on_delete=models.SET_NULL, null=True, default=None, blank=True)

    def __str__(self):
        return self.username
#

class Supplier(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(max_length=225, null=True, blank=True)
    region = models.CharField(max_length=255)
    city = models.CharField(max_length=255, null=True)
    street = models.CharField(max_length=255, null=True)
    email = models.CharField(max_length=225)
    phone = models.CharField(max_length=63, null=True)

    def __str__(self):
        return self.name +' '+ self.last_name


class Category(models.Model):
    category_name = models.CharField(max_length=64)
    slug = models.CharField(max_length=64, primary_key=True)
    def __str__(self):
        return self.category_name

class Product(models.Model):
    name = models.CharField(max_length=128, unique=True)
    description = models.TextField()
    categories = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    suppliers = models.ManyToManyField(Supplier)

    def __str__(self):
        return self.name

class Order(models.Model):
    client = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING)
    product = models.ManyToManyField(Product)


