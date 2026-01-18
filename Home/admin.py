from django.contrib import admin
from .models import FriendSuggestions, TopJournalists, JournalistsSuggestions, contuctus,ArticleSuggestions
from import_export.admin import ImportExportModelAdmin

@admin.register(FriendSuggestions)
class FriendSuggestionsAdmin(ImportExportModelAdmin):   
    list_display = ('user', 'suggested_friend', 'rank', 'suggested_at')
    search_fields = ('user__user__username', 'suggested_friend__user__username')
    list_filter = ('suggested_at',)
    ordering = ('-id',)

@admin.register(TopJournalists)
class TopJournalistsAdmin(ImportExportModelAdmin):
    list_display = ('journalist', 'rank', 'featured_at')
    search_fields = ('journalist__user__username',)
    list_filter = ('featured_at',)
    ordering = ('-id',)

@admin.register(JournalistsSuggestions)
class JournalistsSuggestionsAdmin(ImportExportModelAdmin):
    list_display = ('user', 'suggested_journalist', 'rank', 'suggested_at')
    search_fields = ('user__user__username', 'suggested_journalist__user__username')
    list_filter = ('suggested_at',)
    ordering = ('-id',)


@admin.register(contuctus)
class ContuctusAdmin(ImportExportModelAdmin):
    list_display = ('name', 'email', 'subject', 'sent_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('sent_at',)
    ordering = ('-id',)

@admin.register(ArticleSuggestions)
class ArticleSuggestionsAdmin(ImportExportModelAdmin):
    list_display = ('user', 'suggested_article', 'rank', 'suggested_at')
    search_fields = ('user__user__username', 'suggested_article__title')
    list_filter = ('suggested_at',)
    ordering = ('-id',)