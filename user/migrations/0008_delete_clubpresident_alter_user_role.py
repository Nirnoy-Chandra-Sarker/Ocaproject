# Generated by Django 4.2.2 on 2023-08-19 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_clubpresident_alter_user_role'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ClubPresident',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('ADMIN', 'Admin'), ('ADVISOR', 'Advisor'), ('STUDENT', 'Student')], max_length=20),
        ),
    ]
