from .models import Mijoz
from django.contrib import admin


class MijozAdmin(admin.ModelAdmin):
    list_display = ('ism', 'nomer','email','created_at','comment')
    search_fields = ['ism', 'telefon','created_at']


admin.site.register(Mijoz, MijozAdmin)
