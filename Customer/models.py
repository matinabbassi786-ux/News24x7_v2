from django.db import models
from django.contrib.auth.models import User



class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    firnds = models.ManyToManyField(User, related_name='friends',blank=True)
    OTP = models.CharField(max_length=6, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    is_online = models.BooleanField(default=False)
    status_choices = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('banned', 'Banned'),
    ]
    status = models.CharField(max_length=10, choices=status_choices, default='active')
    Language_choices = [
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('zh', 'Chinese'),
        ('hi', 'Hindi'),
    ]
    preferred_language = models.CharField(max_length=2, choices=Language_choices, default='en')
    age = models.PositiveIntegerField(null=True, blank=True)
    Gender_choices = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=Gender_choices, null=True, blank=True)
    jioing_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username
    
class Frend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')
    frend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='frend_user')
    added_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} is frend with {self.frend.username}"

class messaging(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"From {self.sender.username} to {self.receiver.username} at {self.timestamp}"
    

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Notification for {self.user.username}: {self.message}"

class BlockedUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocker')
    blocked_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blocked')
    blocked_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} blocked {self.blocked_user.username}"


class Token(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Token = models.PositiveIntegerField(default=250000)
    IP = models.GenericIPAddressField(null=True, blank=True)
    data = models.DateTimeField()
    def __str__(self):
        return f"{self.user.username} - {self.Token} tokens"

class TokenHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    page = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)
    IP = models.GenericIPAddressField(null=True, blank=True)
    def __str__(self):
        return f"{self.user.username} - {self.page} on {self.date}"
    

class FrendList(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name="friend_list0")
    frend = models.ManyToManyField(User,related_name="friends0",blank=True)