# Generated by Django 2.0.6 on 2018-10-01 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_line_item_t_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='proposal',
            name='down_payment',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
