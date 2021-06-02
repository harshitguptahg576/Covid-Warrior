# Generated by Django 3.2.2 on 2021-05-16 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('covid', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=50)),
                ('subcategory', models.CharField(max_length=50)),
                ('product_desc', models.CharField(max_length=300)),
                ('product_price', models.IntegerField()),
                ('product_image', models.ImageField(height_field='200px', upload_to='static\\images', width_field='200px')),
            ],
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_image',
            field=models.ImageField(default='', height_field='200px', upload_to='static\\images', width_field='200px'),
        ),
        migrations.AddField(
            model_name='medicine',
            name='medicine_price',
            field=models.IntegerField(default=0),
        ),
    ]