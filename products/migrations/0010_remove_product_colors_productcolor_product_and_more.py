# Generated by Django 5.0.6 on 2024-07-12 18:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_remove_image_image_color_remove_image_image_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='colors',
        ),
        migrations.AddField(
            model_name='productcolor',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_color', to='products.product'),
        ),
        # migrations.CreateModel(
        #     name='ProductSize',
        #     fields=[
        #         ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        #         ('created_on', models.DateTimeField(auto_now=True)),
        #         ('updated_on', models.DateTimeField(auto_now_add=True)),
        #         ('title', models.CharField(max_length=500)),
        #         ('disabled', models.BooleanField(default=False)),
        #         ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_size', to='products.product')),
        #     ],
        #     options={
        #         'verbose_name_plural': 'Product Colors',
        #     },
        # ),
    ]
