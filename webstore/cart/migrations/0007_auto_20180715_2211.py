# Generated by Django 2.0 on 2018-07-15 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_auto_20180707_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='session',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]