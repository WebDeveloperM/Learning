from django.db import models
from django.contrib.auth.models import AbstractUser
from users.utils.fields import expires_default
from users.utils import tokens


class User(AbstractUser):
    TEACHER = 'teacher'
    STUDENT = 'student'
    DIRECTOR = 'director'

    TYPES = (
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
        (DIRECTOR, 'Director')
    )
    REQUIRED_FIELDS = ['phone', 'email']

    phone = models.CharField(max_length=15, unique=True)
    type = models.CharField(max_length=50, choices=TYPES)
    dispatch_id = models.TextField(null=True, blank=True)

    class Meta(AbstractUser.Meta):
        db_table = 'users_user'
        app_label = 'users'

    def __str__(self):
        return f'{self.type}, {self.phone}'


class SmsCode(models.Model):
    dispatch_id = models.CharField(max_length=8)
    code = models.CharField(max_length=4)

    def __str__(self):
        return self.code

    class Meta:
        db_table = 'sms_code'


class Token(models.Model):
    key = models.CharField(max_length=40, unique=True)
    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, models.CASCADE, related_name='tokens')
    expires_at = models.DateTimeField(default=expires_default)  # token expires in 30 days

    def save(self, *args, **kwargs):
        if not self.key:
            self.key = tokens.generate()
        return super(Token, self).save(*args, **kwargs)

    def __str__(self):
        return self.key

    class Meta:
        db_table = 'user_tokens'