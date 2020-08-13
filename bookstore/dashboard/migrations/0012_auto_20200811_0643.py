# Generated by Django 3.1 on 2020-08-11 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_book_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target', models.IntegerField()),
                ('name', models.CharField(max_length=32)),
                ('description', models.CharField(max_length=64)),
                ('datetime', models.DateField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.RenameField(
            model_name='book',
            old_name='status',
            new_name='tracking',
        ),
    ]