# Generated by Django 3.0.3 on 2020-02-07 10:34

from __future__ import unicode_literals
from django.db import models, migrations

def load_users(apps, schema_editor):
    from django.core.management import call_command
    call_command("loaddata", "accounts")

def delete_users(apps, schema_editor):
    CustomUser = apps.get_model("accounts", "CustomUser")
    CustomUser.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_users, delete_users),
    ]