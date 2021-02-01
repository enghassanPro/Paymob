from django.contrib import admin
from .models.user import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models.promo import Promo


class CustomUserAdmin(UserAdmin):
    '''
        Customize user admin in site admin
    '''
    list_display = ('username', 'email', 'is_staff', 'is_active',)
    list_display_links = ('username', 'email',)
    list_filter = ('email', 'is_staff', 'is_active',)
    readonly_fields = ['date_joined', 'last_login', 'password']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser',),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined', 'date_expired')}),
    )

    search_fields = ('email',)
    ordering = ('email',)

# Register your models here.
admin.site.register(User)
admin.site.register(Promo)
