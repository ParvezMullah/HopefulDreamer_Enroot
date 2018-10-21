from django.db import models
from productsapp.models import Product
# Create your models here.


class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField()
    flat_building = models.CharField(
        'Flat No / Building No', max_length=50)
    area = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    rating = models.IntegerField(default=0)
    rating_number = models.IntegerField(default=0)


# class WishList(models.Model):
#     id = models.AutoField(primary_key=True)
#     user_id = models.IntegerField()
#     product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
