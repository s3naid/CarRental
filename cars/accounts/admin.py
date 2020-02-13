from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('email', 'email', 'first_name', 'last_name')  # Contain only fields in your `custom-user-model`
    list_filter = ('is_staff', 'is_superuser', 'is_active')  # Contain only fields in your `custom-user-model` intended for filtering. Do not include `groups`since you do not have it
    search_fields = ('email', 'first_name', 'last_name', 'email')  # Contain only fields in your `custom-user-model` intended for searching
    ordering = ('email',)  # Contain only fields in your `custom-user-model` intended to ordering
    filter_horizontal = () # Leave it empty. You have neither `groups` or `user_permissions`
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login',)}),
    )


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = CustomUser


admin.site.register(CustomUser, CustomUserAdmin)

