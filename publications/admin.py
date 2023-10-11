from django.contrib import admin
from .models import Publication
# Register your models here.

@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title', 'subtitle', 'account','created_at','updated_at')
    list_filter =('title','created_at',)

