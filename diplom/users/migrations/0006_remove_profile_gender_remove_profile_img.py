# Generated by Django 4.0.5 on 2022-07-18 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_remove_profile_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='img',
        ),
    ]
