# Generated by Django 4.2.7 on 2023-12-20 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_status',
            field=models.CharField(max_length=20),
        ),
    ]