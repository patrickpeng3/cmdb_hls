# Generated by Django 4.0 on 2022-07-21 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmdb_auth', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auth_group',
            old_name='enable',
            new_name='status',
        ),
    ]
