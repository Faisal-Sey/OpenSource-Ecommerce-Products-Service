# Generated by Django 5.0.6 on 2024-08-05 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_productcartitem_productcart'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcart',
            old_name='cart_item',
            new_name='cart_items',
        ),
    ]
