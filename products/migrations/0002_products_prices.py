# Generated by Django 2.1.7 on 2019-03-02 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='prices',
            field=models.DecimalField(decimal_places=2, default=39.99, max_digits=20),
        ),
    ]
