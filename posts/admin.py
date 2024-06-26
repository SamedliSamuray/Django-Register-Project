from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Posts)
admin.site.register(Comment)
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'sent_at')
    list_filter = ('sent_at',)
    search_fields = ('name', 'email', 'message')