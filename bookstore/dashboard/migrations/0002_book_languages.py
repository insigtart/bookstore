# Generated by Django 2.2.5 on 2020-07-18 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='languages',
            field=models.ManyToManyField(to='dashboard.Language'),
        ),
    ]
