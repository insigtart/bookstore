# Generated by Django 3.0.7 on 2020-07-28 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20200726_0141'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='status',
            field=models.BooleanField(default=False, null=True, verbose_name='Status carte'),
        ),
    ]
