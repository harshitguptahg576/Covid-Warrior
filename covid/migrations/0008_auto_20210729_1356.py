# Generated by Django 3.2.2 on 2021-07-29 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0007_product_link'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Medicine',
        ),
        migrations.AlterField(
            model_name='product',
            name='link',
            field=models.CharField(default='www.amazon.com', max_length=200),
        ),
    ]
