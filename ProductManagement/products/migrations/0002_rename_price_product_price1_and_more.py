# Generated by Django 4.1.7 on 2024-07-19 21:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='price',
            new_name='price1',
        ),
        migrations.RemoveField(
            model_name='product',
            name='buyer_name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='buyer_number',
        ),
        migrations.RemoveField(
            model_name='product',
            name='payment_status',
        ),
        migrations.RemoveField(
            model_name='product',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='product',
            name='seller',
        ),
        migrations.CreateModel(
            name='Product_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField(default=1)),
                ('buyer_name', models.CharField(max_length=300)),
                ('buyer_number', models.CharField(max_length=11)),
                ('payment_status', models.BooleanField(default=False)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.seller')),
            ],
        ),
    ]
