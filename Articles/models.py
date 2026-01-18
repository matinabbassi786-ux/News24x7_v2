from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from Journalist.models import JournalistInfo
from typing import Optional
from autoslug import AutoSlugField


class Topic(models.Model):
    Topic = models.CharField(max_length=100, unique=True)
    
    created_by = models.ForeignKey(JournalistInfo, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    rank_choices = [
        (-8,"rank -8"),
        (-7,"rank -7"),
        (-6,"rank -6"),
        (-5,"rank -5"),
        (-4,"rank -4"),
        (-3,"rank -3"),
        (-2,"rank -2"),
        (-1,"rank -1"),
        (0,"rank 0"),
        (1,"rank 1"),
        (2,"rank 2"),
        (3,"rank 3"),
        (4,"rank 4"),
        (5,"rank 5"),
        (6,"rank 6"),
        (7,"rank 7"),
        (8,"rank 8"),
    ]
    rank = models.SmallIntegerField(choices=rank_choices, default=0)
    rank_points = models.IntegerField(default=0,validators=[
       MinValueValidator(-8),
        MaxValueValidator(8)
    ])
    def __str__(self):
        return self.Topic

class Article(models.Model):
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(JournalistInfo, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_articles', blank=True)
    likes_count = models.PositiveIntegerField(default=0)
    is_video = models.BooleanField(default=False)
    is_Audio = models.BooleanField(default=False)
    Audios = models.FileField(upload_to='article_audios/', null=True, blank=True)
    viodeo = models.FileField(upload_to='article_videos/', null=True, blank=True)
    image = models.ImageField(upload_to='article_images/', null=True, blank=True)
    image_size = models.CharField(max_length=20, blank=True)
    viodeo_size = models.CharField(max_length=20, blank=True)
    Audio_size = models.CharField(max_length=20, blank=True)
    Audio_length = models.CharField(max_length=20, blank=True)
    slug = AutoSlugField(populate_from='title', unique_with='id', always_update=True)
    rank_choices = [
        (-8,"rank -8"),
        (-7,"rank -7"),
        (-6,"rank -6"),
        (-5,"rank -5"),
        (-4,"rank -4"),
        (-3,"rank -3"),
        (-2,"rank -2"),
        (-1,"rank -1"),
        (0,"rank 0"),
        (1,"rank 1"),
        (2,"rank 2"),
        (3,"rank 3"),
        (4,"rank 4"),
        (5,"rank 5"),
        (6,"rank 6"),
        (7,"rank 7"),
        (8,"rank 8"),
    ]
    rank = models.SmallIntegerField(choices=rank_choices, default=0)
    rank_points = models.IntegerField(default=0,validators=[
       MinValueValidator(-8),
        MaxValueValidator(8)
    ])
    def __str__(self):
        return self.title

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_comments', blank=True)
    likes_count = models.PositiveIntegerField(default=0)
    def __str__(self):
        return f'Comment by {self.user.username} on {self.article.title}'

class ArticleReport(models.Model):
    REASON_CHOICES = [
        ('SPAM', 'Spam or misleading'),
        ('INAPPROPRIATE', 'Inappropriate content'),
        ('COPYRIGHT', 'Copyright violation'),
        ('OTHER', 'Other'),
    ]
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Report on {self.article.title} by {self.reported_by.username}'
    
class CommentReport(models.Model):
    REASON_CHOICES = [
        ('SPAM', 'Spam or misleading'),
        ('INAPPROPRIATE', 'Inappropriate content'),
        ('HARASSMENT', 'Harassment or bullying'),
        ('OTHER', 'Other'),
    ]
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reason = models.CharField(max_length=20, choices=REASON_CHOICES)
    reported_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reported_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Report on comment by {self.comment.user.username} by {self.reported_by.username}'  
    
class bookmarkArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='bookmarks')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookmarked_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Bookmark of {self.article.title} by {self.user.username}'

class followArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='follows')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Follow of {self.article.title} by {self.user.username}'
    
class FollowTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='topic_follows')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Follow of topic {self.topic.Topic} by {self.user.username}'

class multipleImageArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='additional_images')
    image = models.ImageField(upload_to='article_additional_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Additional image for {self.article.title}'

class  multipleViodeoArticle(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='additional_videos')
    viodeo = models.FileField(upload_to='article_additional_videos/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Additional video for {self.article.title}'



class ArticleHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} viewed {self.article.title} at {self.viewed_at}"


class TrendingTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Trending Topic: {self.topic.Topic} with rank {self.rank}"