# Generated by Django 2.0.5 on 2018-10-20 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productsapp', '0004_auto_20181020_1814'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='product_id',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='productid',
        ),
        migrations.AlterField(
            model_name='product',
            name='seller_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='Review',
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
    ]