# Generated by Django 5.1.1 on 2024-09-15 18:46

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kgl', '0003_alter_deffered_payments_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockx',
            name='image',
        ),
        migrations.AlterField(
            model_name='deffered_payments',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 9, 15, 21, 46, 12, 635756)),
        ),
        migrations.AlterField(
            model_name='deffered_payments',
            name='date_of_payment',
            field=models.DateField(default=datetime.datetime(2024, 9, 15, 21, 46, 12, 635756)),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('branch_name', models.CharField(blank=True, max_length=50, null=True)),
                ('seller', models.CharField(blank=True, max_length=50, null=True)),
                ('quantity', models.IntegerField(blank=True, default=10, null=True)),
                ('amount_received', models.IntegerField(blank=True, default=10, null=True)),
                ('issued_to', models.CharField(blank=True, max_length=50, null=True)),
                ('unit_price', models.IntegerField(blank=True, default=10, null=True)),
                ('date', models.DateField(default=datetime.datetime(2024, 9, 15, 21, 46, 12, 634163))),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kgl.stockx')),
            ],
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
    ]
