# Generated by Django 2.0.6 on 2018-09-24 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_line_item_door_handle_cutout'),
    ]

    operations = [
        migrations.AddField(
            model_name='line_item',
            name='resaque_lframe',
            field=models.BooleanField(default=False),
        ),
    ]