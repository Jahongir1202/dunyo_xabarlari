# accounts/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.html import format_html
from .models import CustomUser
from .views import export_users_excel
from django.contrib.auth.models import User

from django.http import HttpResponseRedirect
from django.urls import reverse

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'date_joined']





admin.site.register(CustomUser, CustomUserAdmin)
