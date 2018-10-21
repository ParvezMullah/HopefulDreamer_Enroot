from django.db import models

# Create your models here.


class Seller(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=40)
    mobile = models.CharField(max_length=10)
    gst_name = models.CharField(
        'GST No. ', max_length=15, blank=True, null=True)
    company_or_brand = models.CharField(
        'Company or Brand Name', max_length=30,)
    rank = models.IntegerField(default=0)

    def __str__(self):
        return self.full_name
