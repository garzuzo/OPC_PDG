# Generated by Django 2.2.4 on 2019-10-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opcapp', '0002_auto_20191026_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='zoneType',
            field=models.CharField(choices=[('Rural', 'Rural'), ('Urbana', 'Urbana')], max_length=30),
        ),
    ]
