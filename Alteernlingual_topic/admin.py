from django.contrib import admin


# Register your models here.
from .models import Topic, PolicyConditions
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')

    def email(self, obj):
        try:
            return obj.socialaccount_set.filter(provider='facebook').first().extra_data['email']
        except:
            return None

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


admin.site.register(Topic)
admin.site.register(PolicyConditions)




