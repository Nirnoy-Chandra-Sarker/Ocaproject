# Generated by Django 4.2.2 on 2023-08-11 13:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0020_rename_venue_event_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='room',
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('UB20202', 'UB20202'), ('UB60101', 'UB60101'), ('UB60909', 'UB60909')], max_length=50)),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='club.club')),
                ('event', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='club.event')),
            ],
        ),
    ]