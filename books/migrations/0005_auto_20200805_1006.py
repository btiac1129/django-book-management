# Generated by Django 3.0.8 on 2020-08-05 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20200804_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isOnload',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='reservation_number',
            field=models.IntegerField(default=0),
        ),
    ]
