# Generated by Django 2.0 on 2019-06-15 04:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20190613_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='Date_Purchased',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
