# Generated by Django 4.2.2 on 2023-06-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='marca',
            name='image',
            field=models.ImageField(upload_to='marca_imgs/'),
        ),
    ]
