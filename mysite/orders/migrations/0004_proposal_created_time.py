# Generated by Django 2.0.6 on 2018-09-24 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20180921_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='created_time',
            field=models.TimeField(default=datetime.time(11, 34, 24, 171040)),
        ),
    ]
