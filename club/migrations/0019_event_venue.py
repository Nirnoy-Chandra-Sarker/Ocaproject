# Generated by Django 4.2.2 on 2023-08-11 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0018_sponsor_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='venue',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]