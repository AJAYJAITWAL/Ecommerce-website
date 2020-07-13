# Generated by Django 3.0.2 on 2020-04-19 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='desc',
            field=models.CharField(max_length=300),
        ),
    ]
