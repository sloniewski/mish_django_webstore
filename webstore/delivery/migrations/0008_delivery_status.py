# Generated by Django 2.0 on 2018-07-25 20:23

from django.db import migrations, models
import webstore.delivery.models


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0007_auto_20180725_2009'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivery',
            name='status',
            field=models.CharField(choices=[('AWAITING_PAYMENT', 'awaiting payment'), ('READY_FOR_SHIPPING', 'ready for shipping'), ('SHIPPED', 'shipped')], default=webstore.delivery.models.DeliveryStatus('awaiting payment'), max_length=32),
        ),
    ]
