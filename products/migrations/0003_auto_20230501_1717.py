# Generated by Django 3.2.18 on 2023-05-01 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]
