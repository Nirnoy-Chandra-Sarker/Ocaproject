# Generated by Django 4.2.3 on 2023-07-30 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('club', '0006_clubinfo_delete_achivements'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='short_name',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='clubinfo',
            name='photo',
            field=models.ImageField(upload_to='club_photo/'),
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='achivements/')),
                ('title', models.CharField(max_length=200)),
                ('achieved_date', models.DateField()),
                ('club', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='club.club')),
            ],
        ),
    ]