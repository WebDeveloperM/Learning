from django.db import models
from users.models import User

from apps.main.querysets.student import StudentQuerySet


# Create your models here.


class Science(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="science_user")
    photo = models.FileField(upload_to="sciences", null=True)

    def __str__(self):
        return self.title


class Lesson(models.Model):
    science = models.ForeignKey(Science, on_delete=models.CASCADE, related_name='lesson_science')
    started_datetime = models.DateTimeField(null=True)
    finished_datetime = models.DateTimeField(null=True)
    group = models.ForeignKey("Group", on_delete=models.CASCADE, related_name="lesson_group")

    def __str__(self):
        return self.science.title


class Group(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='student_user')
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='student_group')

    objects = StudentQuerySet.as_manager()

    def __str__(self):
        return self.user.email


class Question(models.Model):
    text = models.TextField()
    science = models.ForeignKey(Science, on_delete=models.CASCADE, related_name="question_science")
    question_time = models.TimeField(null=True)

    def __str__(self):
        return self.text


class Option(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='option_question')
    correct = models.BooleanField(Question, default=False)

    def __str__(self):
        return self.text


class Control(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='control_student')
    science = models.ForeignKey(Science, on_delete=models.CASCADE, related_name='control_science')

    def __str__(self):
        return self.student.email


class Answer(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, related_name='answer_student')
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer_question')
    option = models.ForeignKey(Option, on_delete=models.CASCADE, related_name='answer_option')
    correct = models.BooleanField(default=False)
    response_time = models.TimeField(null=True)

    def __str__(self):
        return self.question.text
