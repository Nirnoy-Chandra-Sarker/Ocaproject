# Generated by Django 4.2.2 on 2023-08-11 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0019_event_venue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='venue',
            new_name='address',
        ),
    ]
