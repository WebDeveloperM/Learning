# Generated by Django 4.2.6 on 2023-10-14 12:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_remove_answer_control_alter_question_science'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.student'),
        ),
    ]
