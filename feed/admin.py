from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import ClientUser

admin.site.register(ClientUser, UserAdmin)
