# Generated by Django 2.2.4 on 2019-10-26 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcapp', '0003_auto_20191026_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
