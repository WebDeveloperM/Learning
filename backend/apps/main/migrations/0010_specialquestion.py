# Generated by Django 4.2.6 on 2023-10-14 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_science_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialQuestion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('question_time', models.TimeField(null=True)),
                ('level', models.CharField(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')], max_length=50)),
                ('science', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='special_question_science', to='main.science')),
            ],
        ),
    ]
