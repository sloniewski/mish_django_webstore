# Generated by Django 2.0.2 on 2018-12-15 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20181215_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='number',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
