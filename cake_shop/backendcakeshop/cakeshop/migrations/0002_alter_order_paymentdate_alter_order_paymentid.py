# Generated by Django 4.2.1 on 2023-05-05 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakeshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='paymentdate',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='paymentid',
            field=models.IntegerField(null=True),
        ),
    ]
