from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username','email','is_superuser','created_at',)
    list_filter = ('is_superuser', 'created_at')
    
   

admin.site.register(User , UserAdmin)