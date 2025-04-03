from django.contrib import admin
from .models import UserProfile, Articles


# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Articles)

