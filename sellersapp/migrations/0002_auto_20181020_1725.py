# Generated by Django 2.0.5 on 2018-10-20 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellersapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seller',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
