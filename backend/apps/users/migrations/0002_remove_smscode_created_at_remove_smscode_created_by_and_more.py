# Generated by Django 4.2.6 on 2023-10-13 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='smscode',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='smscode',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='smscode',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='smscode',
            name='updated_by',
        ),
    ]
