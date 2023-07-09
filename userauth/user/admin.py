from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import registrationModel

@admin.register(registrationModel)
class registrationAdmin(UserAdmin):
    model = registrationModel
    list_display = ['username', 'first_name', 'last_name', 'email']
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            "fields": (
                'mobile_number',
            ),
        }),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            "fields": (
                'mobile_number',
            ),
        }),
    )
    


