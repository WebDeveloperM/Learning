# Generated by Django 4.2.6 on 2023-10-14 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_option_response_time_question_question_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='response_time',
        ),
        migrations.AddField(
            model_name='answer',
            name='response_time',
            field=models.TimeField(null=True),
        ),
    ]