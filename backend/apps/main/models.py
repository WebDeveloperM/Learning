from django.db import models
from users.models import User

from apps.main.querysets.student import StudentQuerySet


# Create your models here.


class Science(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="User")

    def __str__(self):
        return self.title


class Lesson(models.Model):
    science = models.ForeignKey(Science, on_delete=models.CASCADE)
    started_date = models.DateField(null=True)
    started_time = models.TimeField(null=True)
    finished_date = models.DateTimeField()
    group = models.ForeignKey("Group", on_delete=models.CASCADE)

    def __str__(self):
        return self.science.title


class Group(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    objects = StudentQuerySet.as_manager()

    def __str__(self):
        return self.user.email


class Question(models.Model):
    text = models.TextField()
    science = models.ForeignKey(Science, on_delete=models.CASCADE, related_name="science")
    question_time = models.TimeField(null=True)

    def __str__(self):
        return self.text


class Option(models.Model):
    text = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    correct = models.BooleanField(Question, default=False)

    def __str__(self):
        return self.text


class Control(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    science = models.ForeignKey(Science, on_delete=models.CASCADE)

    def __str__(self):
        return self.student.email


class Answer(models.Model):
    control = models.ForeignKey(Control, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    correct = models.BooleanField(default=False)
    response_time = models.TimeField(null=True)

    def __str__(self):
        return self.question.text
