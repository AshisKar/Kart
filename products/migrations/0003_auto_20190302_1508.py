# Generated by Django 2.1.7 on 2019-03-02 09:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_prices'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
