from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from myapp import models

admin.site.register(models.Tenant)
admin.site.register(models.Domain)


@admin.register(models.TenantUser)
class TenantUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password', 'tenant')}),
    )
    list_display = ['username']
    search_fields = ['username']
    filter_horizontal = []
    list_filter = ['username']
