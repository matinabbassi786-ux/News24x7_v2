from django.contrib import admin
from .models import languageoptions,translation
from import_export.admin import ImportExportModelAdmin


@admin.register(languageoptions)
class LanguageOptionsAdmin(ImportExportModelAdmin):
    list_display = ('language',)
    search_fields = ('language',)
    ordering = ('-id',)
    
@admin.register(translation)
class TranslationAdmin(ImportExportModelAdmin):
    list_display = ('article', 'target_language', 'translated_at')
    search_fields = ('article__title', 'target_language__language')
    list_filter = ('target_language', 'translated_at')
    ordering = ('-id',)