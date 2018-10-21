from django.db import models
from django.utils import timezone
from sellersapp.models import Seller
# Create your models here.


class Product(models.Model):

    categories = (
        ('cloths', 'Cloths'),
        ('show piece', 'Show Piece'),
        ('home appliance', 'Home Appliance'),
        ('solar product', 'Solar Product'),
        ('accessories', 'Accessories')
    )
    product_id = models.AutoField(primary_key=True)
    seller_id = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=categories)
    price = models.IntegerField()
    picture = models.ImageField(blank=True, null=True)
    date_first_available = models.CharField(
        "Date First Available", max_length=500, default='20/10/2018')
    description = models.TextField(max_length=300)
    quantities_available = models.IntegerField('Availabe Quantities')

    def __str__(self):
        return self.title


# class Review(models.Model):
#     id = models.AutoField(primary_key=True)
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
#     user_id = models.IntegerField()
#     rating = models.IntegerField()
#     review_title = models.CharField(max_length=50)
#     description = models.TextField(max_length=300)

#     class Meta:
#         verbose_name_plural = 'Reviews'

#     def __str__(self):
#         return self.name


# class Transactions(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.IntegerField()
#     productid = models.ForeignKey(Product, on_delete=models.CASCADE)


class Post(models.Model):

    post_id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=7)
    title = models.CharField(max_length=200)
    picture = models.ImageField(blank=True, null=True)
    date_published = models.CharField(
        "Date First Available", max_length=50, default=timezone.now)
    description = models.TextField(max_length=300)
    contact_number = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    quantities_available = models.IntegerField(
        'Availabe Quantities', blank=True, null=True)
    quantity_weight = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title
