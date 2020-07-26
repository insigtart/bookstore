# Generated by Django 3.0.8 on 2020-07-25 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20200722_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=64, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='book',
            name='datetime',
            field=models.DateField(verbose_name='Data publicării'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Detalii'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=256, verbose_name='Titlu'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Țări'),
        ),
        migrations.AlterField(
            model_name='language',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Limbi'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='name',
            field=models.CharField(max_length=256, unique=True, verbose_name='Catwgorii'),
        ),
    ]
