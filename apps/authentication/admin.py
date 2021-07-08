from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.authentication.forms import CustomUserCreationForm, \
    CustomUserChangeForm
from apps.authentication.models import User


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('phone_number', 'is_staff', 'is_active',)
    list_filter = ('phone_number', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'phone_number', 'password1', 'password2', 'is_staff',
                'is_active')}
         ),
    )
    search_fields = ('phone_number',)
    ordering = ('phone_number',)


admin.site.register(User, CustomUserAdmin)
