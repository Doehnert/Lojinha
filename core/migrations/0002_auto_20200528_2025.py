# Generated by Django 2.2.10 on 2020-05-28 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='points',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='buy_with_points',
        ),
    ]
