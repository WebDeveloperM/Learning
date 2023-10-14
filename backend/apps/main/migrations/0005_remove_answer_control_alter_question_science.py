# Generated by Django 4.2.6 on 2023-10-14 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_lesson_started_time_alter_lesson_started_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='control',
        ),
        migrations.AlterField(
            model_name='question',
            name='science',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='science', to='main.science'),
        ),
    ]