from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import UserInfo, Frend, messaging, Notification,Token,TokenHistory,BlockedUser,FrendList

@admin.register(UserInfo)
class UserInfoAdmin(ImportExportModelAdmin):
    list_display = ('user', 'is_verified', 'is_online', 'status', 'preferred_language', 'age', 'gender')
    search_fields = ('user__username', 'user__email', 'status', 'preferred_language', 'gender')
    list_filter = ('is_verified', 'is_online', 'status', 'preferred_language', 'gender')    
    ordering = ('user__username',)

@admin.register(Frend)
class FrendAdmin(ImportExportModelAdmin):
    list_display = ('user', 'frend', 'added_at')
    search_fields = ('user__username', 'frend__username')
    list_filter = ('added_at',)
    ordering = ('-added_at',)

@admin.register(messaging)
class MessagingAdmin(ImportExportModelAdmin):
    list_display = ('sender', 'receiver', 'timestamp', 'is_read')
    search_fields = ('sender__username', 'receiver__username', 'message')
    list_filter = ('is_read', 'timestamp')
    ordering = ('-timestamp',)

@admin.register(Notification)
class NotificationAdmin(ImportExportModelAdmin):
    list_display = ('user', 'message', 'is_read')
    search_fields = ('user__username', 'message')
    list_filter = ('is_read',)
    ordering = ('-id',)


@admin.register(BlockedUser)
class BlockedUserAdmin(ImportExportModelAdmin):
    list_display = ('user', 'blocked_user', 'blocked_at')
    search_fields = ('user__username', 'blocked_user__username')
    list_filter = ('blocked_at',)
    ordering = ('-id',)

@admin.register(Token)
class TokenAdmin(ImportExportModelAdmin):
    list_display = ('user', 'Token', 'data')
    search_fields = ('user__username', 'Token')
    list_filter = ('user',)
    ordering = ('-id',)

@admin.register(TokenHistory)
class TokenHistoryAdmin(ImportExportModelAdmin):
    list_display = ('user', 'page', 'date', 'IP')
    search_fields = ('user__username', 'page', 'IP')
    list_filter = ('date',)
    ordering = ('-id',)

