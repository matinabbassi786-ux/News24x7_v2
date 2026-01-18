from django.contrib import admin
from .models import Article, Topic, Comment,ArticleReport,CommentReport,bookmarkArticle,followArticle,FollowTopic,multipleImageArticle,multipleViodeoArticle,ArticleHistory,TrendingTopic
from import_export.admin import ImportExportModelAdmin



@admin.register(Article)
class ArticleAdmin(ImportExportModelAdmin):
    list_display = ('title', 'author', 'published_date', 'likes_count', 'is_video')
    search_fields = ('title', 'author__user__username', 'content')
    list_filter = ('is_video', 'published_date')
    ordering = ('-id',) 

@admin.register(Topic)
class TopicAdmin(ImportExportModelAdmin):
    list_display = ('Topic', 'created_by', 'created_at')
    search_fields = ('Topic', 'created_by__user__username')
    list_filter = ('created_at',)
    ordering = ('id',)

@admin.register(Comment)
class CommentAdmin(ImportExportModelAdmin):
    list_display = ('article', 'user', 'created_at')
    search_fields = ('article__title', 'user__username', 'content')
    list_filter = ('created_at',)
    ordering = ('-id',)

@admin.register(ArticleReport)
class ArticleReportAdmin(ImportExportModelAdmin):
    list_display = ('article', 'reason', 'reported_by', 'reported_at')
    search_fields = ('article__title', 'reported_by__username', 'reason')
    list_filter = ('reason', 'reported_at')
    ordering = ('-id',)

@admin.register(CommentReport)
class CommentReportAdmin(ImportExportModelAdmin):
    list_display = ('comment', 'reason', 'reported_by', 'reported_at')
    search_fields = ('comment__content', 'reported_by__username', 'reason')
    list_filter = ('reason', 'reported_at')
    ordering = ('-id',)

@admin.register(bookmarkArticle)
class BookmarkArticleAdmin(ImportExportModelAdmin):
    list_display = ('article', 'user', 'bookmarked_at')
    search_fields = ('article__title', 'user__username')
    list_filter = ('bookmarked_at',)
    ordering = ('-id',)

@admin.register(followArticle)
class FollowArticleAdmin(ImportExportModelAdmin):
    list_display = ('article', 'user', 'followed_at')
    search_fields = ('article__title', 'user__username')
    list_filter = ('followed_at',)
    ordering = ('-id',)


@admin.register(FollowTopic)
class FollowTopicAdmin(ImportExportModelAdmin):
    list_display = ('topic', 'user', 'followed_at')
    search_fields = ('topic__Topic', 'user__username')
    list_filter = ('followed_at',)
    ordering = ('-id',)

@admin.register(multipleImageArticle)
class MultipleImageArticleAdmin(ImportExportModelAdmin):
    list_display = ('article', 'image', 'uploaded_at')
    search_fields = ('article__title',)
    list_filter = ('uploaded_at',)
    ordering = ('-id',)

@admin.register(multipleViodeoArticle)
class MultipleViodeoArticleAdmin(ImportExportModelAdmin):
    list_display = ('article', 'viodeo', 'uploaded_at')
    search_fields = ('article__title',)
    list_filter = ('uploaded_at',)
    ordering = ('-id',)


@admin.register(ArticleHistory)
class ArticleHistoryAdmin(ImportExportModelAdmin):
    list_display = ('article', 'user', 'viewed_at')
    search_fields = ('article__title', 'user__username')
    list_filter = ('viewed_at',)
    ordering = ('-id',)

@admin.register(TrendingTopic)
class TrendingTopicAdmin(ImportExportModelAdmin):
    list_display = ('topic',  'updated_at')
    search_fields = ('topic__Topic',)
    list_filter = ('updated_at',)
    ordering = ('-id',)
