# Generated by Django 2.0.2 on 2018-03-17 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0002_auto_20180318_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='icon',
            field=models.ImageField(storage='/media/', upload_to='', verbose_name='Иконка'),
        ),
        migrations.AlterField(
            model_name='cafe',
            name='pic',
            field=models.ImageField(storage='/media/', upload_to='', verbose_name='Фото'),
        ),
    ]
