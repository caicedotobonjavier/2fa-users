from django.contrib import admin
#
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'id_user',
        'email',
        'full_name',
        'date_birth',
        'address',
        'phone',
        'is_staff',
        'is_active',
        'is_superuser',
    )

admin.site.register(User, UserAdmin)