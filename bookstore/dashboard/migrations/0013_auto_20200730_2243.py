# Generated by Django 3.0.3 on 2020-07-30 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20200730_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='description',
            field=models.CharField(max_length=64),
        ),
    ]
