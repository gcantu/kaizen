# Generated by Django 2.0.6 on 2018-09-20 02:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=25)),
            ],
            options={
                'db_table': 'agent',
            },
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('address', models.CharField(blank=True, max_length=255)),
                ('city', models.CharField(blank=True, max_length=255)),
                ('zip_code', models.CharField(blank=True, max_length=5)),
                ('home_phone', models.CharField(blank=True, max_length=25)),
                ('mobile_phone', models.CharField(blank=True, max_length=25)),
                ('email', models.EmailField(blank=True, max_length=254)),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='line_item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=100)),
                ('mount', models.CharField(blank=True, choices=[('Int', 'Interior'), ('Ext', 'Exterior')], max_length=3)),
                ('trim', models.IntegerField(blank=True, choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4')], null=True)),
                ('trim_style', models.CharField(blank=True, choices=[('Deco', 'Decorative'), ('Square', 'Square (Smooth)'), ('Round', 'Round (Smooth)'), ('Z', 'Z (Primed)'), ('Other', 'Other')], max_length=10)),
                ('panels', models.IntegerField(blank=True, null=True)),
                ('width', models.IntegerField(blank=True, null=True)),
                ('height', models.IntegerField(blank=True, null=True)),
                ('height_left', models.IntegerField(blank=True, null=True)),
                ('height_right', models.IntegerField(blank=True, null=True)),
                ('height_center', models.IntegerField(blank=True, null=True)),
                ('width_fraction', models.FloatField(choices=[(0, ''), (0.125, '1/8'), (0.25, '1/4'), (0.375, '3/8'), (0.5, '1/2'), (0.625, '5/8'), (0.75, '3/4'), (0.875, '7/8')], default=0)),
                ('height_fraction', models.FloatField(choices=[(0, ''), (0.125, '1/8'), (0.25, '1/4'), (0.375, '3/8'), (0.5, '1/2'), (0.625, '5/8'), (0.75, '3/4'), (0.875, '7/8')], default=0)),
                ('height_left_fraction', models.FloatField(choices=[(0, ''), (0.125, '1/8'), (0.25, '1/4'), (0.375, '3/8'), (0.5, '1/2'), (0.625, '5/8'), (0.75, '3/4'), (0.875, '7/8')], default=0)),
                ('height_right_fraction', models.FloatField(choices=[(0, ''), (0.125, '1/8'), (0.25, '1/4'), (0.375, '3/8'), (0.5, '1/2'), (0.625, '5/8'), (0.75, '3/4'), (0.875, '7/8')], default=0)),
                ('height_center_fraction', models.FloatField(choices=[(0, ''), (0.125, '1/8'), (0.25, '1/4'), (0.375, '3/8'), (0.5, '1/2'), (0.625, '5/8'), (0.75, '3/4'), (0.875, '7/8')], default=0)),
                ('price_per_sq_ft', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'line_item',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=45, unique=True)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='proposal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateField(default=datetime.date.today)),
                ('finish', models.CharField(blank=True, choices=[('Paint', 'Paint'), ('Stain', 'Stain')], max_length=5, null=True)),
                ('stain', models.CharField(blank=True, choices=[('Ash', 'Ash'), ('Basswood', 'Basswood'), ('Knotty Alder', 'Knotty Alder'), ('Maple', 'Maple'), ('Pine', 'Pine')], max_length=15, null=True)),
                ('color', models.CharField(blank=True, max_length=100)),
                ('louver', models.FloatField(blank=True, choices=[(2.5, '2 1/2'), (3.5, '3 1/2'), (4.5, '4 1/2')], null=True)),
                ('hinges', models.CharField(blank=True, choices=[('LR', 'Left/Right'), ('L', 'Left'), ('R', 'Right')], max_length=2)),
                ('hinge_color', models.CharField(blank=True, choices=[('Bronze', 'Bronze'), ('Nickel', 'Nickel'), ('White', 'White'), ('Bright White', 'Bright-White'), ('Off White', 'Off-White'), ('No Hinges', 'No Hinges'), ('Other', 'Other')], max_length=15)),
                ('tilt_rod', models.CharField(blank=True, choices=[('Normal', 'Normal'), ('Side and Back', 'Side and Back'), ('Aluminum', 'Aluminum')], max_length=15)),
                ('notes', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved')], default='Pending', max_length=10)),
                ('agents', models.ManyToManyField(to='orders.agent')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.customer')),
                ('measured_by', models.ManyToManyField(related_name='proposal_measured_by', to='orders.agent')),
            ],
            options={
                'db_table': 'proposal',
            },
        ),
        migrations.CreateModel(
            name='shutter_type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shutter_type_name', models.CharField(max_length=100, unique=True)),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.product')),
            ],
            options={
                'db_table': 'shutter_type',
            },
        ),
        migrations.AddField(
            model_name='line_item',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.product'),
        ),
        migrations.AddField(
            model_name='line_item',
            name='proposal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.proposal'),
        ),
        migrations.AddField(
            model_name='line_item',
            name='shutter_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='orders.shutter_type'),
        ),
    ]
