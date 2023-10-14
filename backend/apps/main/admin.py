from django.contrib import admin
from main.models import (
                    Science,
                    Lesson,
                    Student,
                    Group,
                    Question,
                    Option,
                    Control,
                    Answer
                )
# Register your models here.


class AuthorMixin:
    def save_model(self, request, obj, form, change):
        if change:
            obj.updated_by = request.user
        else:
            obj.created_by = request.user

        super().save_model(request, obj, form, change)


@admin.register(Science)
class ScienceAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ('title', 'teacher')
    fields = ('title', 'teacher')


@admin.register(Lesson)
class LessonAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ('science', 'started_date', 'finished_date', 'group')
    fields = ('science', 'started_date', 'finished_date', 'group')


@admin.register(Group)
class GroupAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ['title']
    fields = ['title']


@admin.register(Student)
class Student(AuthorMixin, admin.ModelAdmin):
    list_display = ('user', 'group')
    fields = ('user', 'group')


@admin.register(Question)
class QuestionAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ('text', 'science')
    fields = ('text', 'science')


@admin.register(Option)
class OptionAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ('text', 'question', 'correct')
    fields = ('text', 'question', 'correct')


@admin.register(Control)
class ControlAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ('student', 'science')
    fields = ('student', 'science')


@admin.register(Answer)
class AnswerAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ('control', 'question', 'option', 'correct')
    fields = ('control', 'question', 'option', 'correct')


