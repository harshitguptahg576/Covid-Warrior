# Generated by Django 3.2.2 on 2021-05-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0003_rename_subcategory_product_manufacturer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='static\\images'),
        ),
    ]
