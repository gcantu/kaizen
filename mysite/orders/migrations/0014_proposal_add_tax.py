# Generated by Django 2.0.6 on 2018-10-01 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_proposal_down_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='add_tax',
            field=models.BooleanField(default=False),
        ),
    ]