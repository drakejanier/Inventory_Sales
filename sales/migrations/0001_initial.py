# Generated by Django 2.0 on 2019-06-15 04:16

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0005_auto_20190615_1216'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Customer', models.CharField(max_length=50)),
                ('Quantity', models.IntegerField(default=0)),
                ('List_Price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('Total_Sales', models.IntegerField(default=0)),
                ('Date_Sold', models.DateTimeField(default=datetime.datetime.now)),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Products')),
                ('User', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SalesList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(default=0)),
                ('Price', models.DecimalField(decimal_places=2, default=0, max_digits=6)),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Products')),
                ('Sales_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sales.Sales')),
            ],
        ),
    ]
