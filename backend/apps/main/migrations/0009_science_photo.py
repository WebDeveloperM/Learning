# Generated by Django 4.2.6 on 2023-10-14 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_lesson_finished_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='science',
            name='photo',
            field=models.FileField(null=True, upload_to='sciences'),
        ),
    ]
