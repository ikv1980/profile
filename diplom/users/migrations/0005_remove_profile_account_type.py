# Generated by Django 4.0.5 on 2022-07-18 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_profile_account_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='account_type',
        ),
    ]
