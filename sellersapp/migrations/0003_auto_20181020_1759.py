# Generated by Django 2.0.5 on 2018-10-20 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellersapp', '0002_auto_20181020_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='userid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
