# Generated by Django 2.2 on 2020-02-03 17:21

from django.db import migrations
from django.core.management import call_command


def update_providers(apps, schema_editor):
    # Clean deprecated deezer provider, delete provider duplicates
    # update provider's fields and ensure item's provider FK
    call_command('timeside-provider-deezer-preview', verbosity=0)


class Migration(migrations.Migration):

    dependencies = [
        ('timeside_server', '0008_auto_fields_help_texts'),
    ]

    operations = [
        migrations.RunPython(update_providers),
    ]