# Generated by Django 3.0.3 on 2020-03-19 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('obsapp', '0002_auto_20200319_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='facility',
            name='date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
