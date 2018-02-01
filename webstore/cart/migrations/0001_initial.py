# Generated by Django 2.0 on 2018-01-07 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0006_auto_20180107_2044'),
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CartItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.Cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ManyToManyField(through='cart.CartItem', to='product.Product'),
        ),
        migrations.AddField(
            model_name='cart',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sessions.Session'),
        ),
    ]