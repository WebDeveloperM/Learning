# Generated by Django 4.2.6 on 2023-10-14 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_specialoption_specialanswer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='science',
            name='photo',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]