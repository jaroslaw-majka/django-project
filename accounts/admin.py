from django.contrib import admin

# Register your models here.
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
