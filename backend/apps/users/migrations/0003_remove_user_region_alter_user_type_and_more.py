# Generated by Django 4.2.6 on 2023-10-13 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_smscode_created_at_remove_smscode_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='region',
        ),
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.CharField(choices=[('teacher', 'Teacher'), ('student', 'Student'), ('director', 'Director')], max_length=50),
        ),
        migrations.AlterModelTable(
            name='smscode',
            table='sms_code',
        ),
    ]