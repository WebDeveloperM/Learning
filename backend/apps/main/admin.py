from django.contrib import admin
from main.models import (
                    Science,
                    Lesson,
                    Student,
                    Group,
                    Question,
                    Option,
                    Control,
                    Answer,
                    SpecialAnswer,
                    SpecialOption,
                    SpecialQuestion
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
    list_display = ('title', 'teacher', 'photo')
    fields = ('title', 'teacher', 'photo')


@admin.register(Lesson)
class LessonAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ('science', 'started_datetime', 'finished_datetime', 'group')
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
    list_display = ('question', 'option', 'correct', 'student')
    fields = ('question', 'option', 'correct', 'student')


@admin.register(SpecialAnswer)
class SpAnswerAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ('student', 'question', 'option', 'correct', 'response_time', 'time_delta' )
    fields = ( 'student', 'question', 'option', 'correct', 'response_time', 'time_delta')


@admin.register(SpecialQuestion)
class QuestionAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ('text', 'science', 'question_time', 'level')
    fields = ('text', 'science', 'question_time', 'level')


@admin.register(SpecialOption)
class OptionAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ('text', 'question', 'correct')
    fields = ('text', 'question', 'correct')
