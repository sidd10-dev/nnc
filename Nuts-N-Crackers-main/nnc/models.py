from django.db import models
from django.db.models.fields import IntegerField
from django.template.defaultfilters import slugify


class Category(models.Model):
    title = models.CharField(max_length=50)
    category_image = models.ImageField(null = True, blank = True)
    heading = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    slug = models.SlugField(null = True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Category,self).save(*args,**kwargs)

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length = 50)
    weight = models.FloatField()
    brand = models.CharField(max_length=50)
    price = models.FloatField()
    product_image = models.ImageField()
    description = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CategoryProduct(models.Model):
    category = models.ForeignKey("nnc.Category",on_delete = models.CASCADE, null = True)
    product = models.ForeignKey("nnc.Product",on_delete=models.CASCADE, null = True)

    def __str__(self):
        return self.category.title + '-' + self.product.name

class Order(models.Model):
    user = models.ForeignKey("auth.User",on_delete = models.CASCADE)
    customer = models.ForeignKey("accounts.customer",on_delete = models.CASCADE)
    complete = models.BooleanField(default = False)
    total = models.IntegerField(default = 0)
    number_of_items = models.IntegerField(default = 0)
    date_ordered = models.DateTimeField(null = True)
    delivered = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username + '-' + str(self.pk)

class OrderProduct(models.Model):
    order = models.ForeignKey("nnc.Order",on_delete = models.CASCADE)
    product = models.ForeignKey("nnc.CategoryProduct",on_delete = models.CASCADE)
    quantity = models.IntegerField(default = 1)

    def __str__(self):
        return str(self.order.pk) + '-' + self.product.product.name

    def calcprice(self):
        return self.quantity * self.product.product.price


