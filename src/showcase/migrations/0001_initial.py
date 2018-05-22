# Generated by Django 2.0 on 2018-05-16 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('comments', models.CharField(default='', max_length=400, verbose_name='Comments')),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('product', models.CharField(max_length=200, verbose_name='Producto')),
                ('idProvider', models.CharField(max_length=36, primary_key=True, serialize=False, unique=True, verbose_name='ID UNICO')),
                ('stock', models.PositiveSmallIntegerField(default=0, verbose_name='Stock Actual')),
                ('minimumStock', models.PositiveSmallIntegerField(default=0, verbose_name='Stock Minimo')),
                ('photo', models.ImageField(default='items/noImage.png', upload_to='items')),
                ('description', models.CharField(default='', max_length=200, verbose_name='Descripción')),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItemQuantityPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=0, verbose_name='Quantity')),
                ('item', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='showcase.Item', verbose_name='Item')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('number', models.CharField(default='', max_length=36, primary_key=True, serialize=False, unique=True, verbose_name='Number')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Date')),
                ('comments', models.CharField(blank=True, default='', max_length=400, verbose_name='Comments')),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=6, verbose_name='Invoice Total (ARS)')),
                ('items', models.ManyToManyField(default=None, to='showcase.ItemQuantityPair', verbose_name='Products')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_AD', models.CharField(max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='User ID')),
                ('mail', models.EmailField(default='', max_length=50, unique=True, verbose_name='Email')),
                ('name', models.CharField(default='', max_length=50, verbose_name='Name')),
                ('last_name', models.CharField(default='', max_length=50, verbose_name='Last Name')),
            ],
        ),
        migrations.AddField(
            model_name='delivery',
            name='items',
            field=models.ManyToManyField(default=None, to='showcase.ItemQuantityPair', verbose_name='Products'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='user',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='showcase.User', verbose_name='User'),
        ),
    ]
