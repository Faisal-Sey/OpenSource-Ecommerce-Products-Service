# Generated by Django 5.0.6 on 2024-08-05 15:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_delete_productdescription_alter_product_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCartItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('quantity', models.IntegerField(default=0)),
                ('total_amount', models.FloatField(default=0.0)),
                ('product_size', models.JSONField(default=dict)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item_product_image', to='products.image')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_item_product', to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('updated_on', models.DateTimeField(auto_now_add=True)),
                ('checkout_url', models.URLField(blank=True)),
                ('total_amount', models.FloatField(default=0.0)),
                ('total_taxed', models.FloatField(default=0.0)),
                ('currency', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_cart_currency', to='products.productcurrency')),
                ('cart_item', models.ManyToManyField(blank=True, related_name='product_cart_item', to='products.productcartitem')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
