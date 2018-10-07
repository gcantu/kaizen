# Generated by Django 2.0.6 on 2018-10-05 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0016_line_item_frame_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line_item',
            name='trim',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], default=0),
        ),
        migrations.AlterField(
            model_name='proposal',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Deleted', 'Deleted')], default='Pending', max_length=10),
        ),
    ]