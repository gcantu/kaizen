# Generated by Django 2.0.6 on 2018-10-05 19:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0017_auto_20181005_1429'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='installation_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]