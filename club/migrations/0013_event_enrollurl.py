# Generated by Django 4.2.3 on 2023-08-02 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0012_alter_event_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='enrollurl',
            field=models.URLField(null=True),
        ),
    ]
