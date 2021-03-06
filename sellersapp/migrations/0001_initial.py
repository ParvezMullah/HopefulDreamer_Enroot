# Generated by Django 2.0.5 on 2018-10-20 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.IntegerField()),
                ('full_name', models.CharField(max_length=40)),
                ('mobile', models.CharField(max_length=10)),
                ('gst_name', models.CharField(blank=True, max_length=15, null=True, verbose_name='GST No. ')),
                ('company_or_brand', models.CharField(max_length=30, verbose_name='Company or Brand Name')),
                ('rank', models.IntegerField()),
            ],
        ),
    ]
