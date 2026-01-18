from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import JournalistInfo


@admin.register(JournalistInfo)
class JournalistInfoAdmin(ImportExportModelAdmin):
    list_display = ('user', 'totlelikes', 'totlenewsarticles', 'rank', 'jioing_date')
    search_fields = ('user__username', 'user__email', 'address', 'phone_number', 'email', 'rank')
    list_filter = ('rank', 'jioing_date')
    ordering = ('-id',)

