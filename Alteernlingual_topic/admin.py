from django.contrib import admin


# Register your models here.
from .models import Topic, PolicyConditions

admin.site.register(Topic)
admin.site.register(PolicyConditions)