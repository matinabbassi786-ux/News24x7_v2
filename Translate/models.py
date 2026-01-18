from django.db import models
from Articles.models import Article
# Create your models here.

class languageoptions(models.Model):
    language = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.language

class translation(models.Model):
    target_language = models.ForeignKey(languageoptions, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    translated_content = models.TextField()
    translated_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Translation of {self.article.title} to {self.target_language.language}"

