# Generated by Django 4.0.5 on 2022-09-07 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('link', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='Идентификатор'),
        ),
    ]
