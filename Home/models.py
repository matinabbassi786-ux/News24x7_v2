from django.db import models
from django.contrib.auth.models import User
from Customer.models import UserInfo
from Articles.models import Article
from Journalist.models import JournalistInfo


class FriendSuggestions(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    suggested_friend = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='suggested_to')
    rank = models.IntegerField()
    suggested_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Suggestion: {self.suggested_friend.user.username} to {self.user.user.username} with rank {self.rank}"

class TopJournalists(models.Model):
    journalist = models.ForeignKey(JournalistInfo, on_delete=models.CASCADE)
    rank = models.PositiveBigIntegerField(unique=True,blank=True,null=True)
    featured_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Top Journalist: {self.journalist.user.username} with rank {self.rank}"


class JournalistsSuggestions(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    suggested_journalist = models.ForeignKey(JournalistInfo, on_delete=models.CASCADE, related_name='suggested_to_users')
    rank = models.IntegerField()
    suggested_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Suggestion: {self.suggested_journalist.user.username} to {self.user.user.username} with rank {self.rank}"


class contuctus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Contact Us Message from {self.name} - {self.subject}"
    

class ArticleSuggestions(models.Model):
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    suggested_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='suggested_to_users')
    rank = models.IntegerField()
    suggested_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Suggestion: {self.suggested_article.title} to {self.user.user.username} with rank {self.rank}"