# Generated by Django 4.2.3 on 2023-07-29 00:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0003_room_achivements'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Room',
            new_name='Event',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='event',
            new_name='eventname',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='roomname',
            new_name='room',
        ),
    ]
