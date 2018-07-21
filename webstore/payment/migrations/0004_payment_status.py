# Generated by Django 2.0 on 2018-07-21 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_payment_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('ne', 'new'), ('op', 'open'), ('cl', 'closed'), ('dl', 'delayed')], default='ne', max_length=16),
        ),
    ]
