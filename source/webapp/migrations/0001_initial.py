# Generated by Django 3.2.15 on 2022-08-08 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(blank=True, max_length=100, verbose_name='Наименование товара')),
                ('product_description', models.TextField(max_length=2000, verbose_name='Описание товара')),
                ('category', models.TextField(blank=True, choices=[('Other', 'Разное'), ('IPad', 'IPad'), ('IPod', 'IPod'), ('IPhone', 'IPhone'), ('AirPods', 'AirPods'), ('MacOS', 'MacOS'), ('Apple Watch', 'Apple Watch')], default='Other', max_length=100, verbose_name='Категория')),
                ('remainder', models.IntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
