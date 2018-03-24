from django.contrib import admin
from .models import Event, User, AuthUser, Branch
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class StaffUserAdmin(UserAdmin):
# ...code here...

    fieldsets = (
        (None, {'fields': ('username', 'password', 'email', 'branch',)}),
        (('Personal info'), {'fields': ('first_name', 'last_name')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'branch')}
         ),
    )

    list_display = ('username', 'first_name', 'email', 'branch', 'is_staff')

    list_filter = ('branch', 'is_staff',)

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'branch', 'time', 'date', 'location', )

    list_filter = ('branch',)

admin.site.register(AuthUser, StaffUserAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(User)
admin.site.register(Branch)