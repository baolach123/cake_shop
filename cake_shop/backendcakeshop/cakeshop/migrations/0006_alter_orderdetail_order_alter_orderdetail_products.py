# Generated by Django 4.2.1 on 2023-05-06 18:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cakeshop', '0005_order_grand_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetail',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cakeshop.order'),
        ),
        migrations.AlterField(
            model_name='orderdetail',
            name='products',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='oderitems', to='cakeshop.products'),
        ),
    ]