from django.contrib import admin

from .models import User, SmsCode
from django.conf import settings
from users.models import Token
from main.admin import AuthorMixin


# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['type']
    fields = ['type']


@admin.register(SmsCode)
class SmscodeAdmin(AuthorMixin, admin.ModelAdmin):
    list_display = ('dispatch_id', 'code')
    fields = ('dispatch_id', 'code')

    def has_add_permission(self, request, obj=None):
        return False


    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Token)