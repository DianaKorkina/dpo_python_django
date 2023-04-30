# Generated by Django 4.2 on 2023-04-30 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0005_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='order', to='shopapp.product'),
        ),
    ]