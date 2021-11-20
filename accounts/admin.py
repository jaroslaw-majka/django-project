# Django
from django.contrib import admin

# Project
from accounts.models import ExtendedUser


@admin.register(ExtendedUser)
class ExtendedUserAdmin(admin.ModelAdmin):
    list_display = (
        'username',
        'email',
    )

    list_editable = (
        'email',
    )
