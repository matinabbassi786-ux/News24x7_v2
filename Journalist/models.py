from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class JournalistInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    followers = models.ManyToManyField(User, related_name='followers', blank=True)
    totlelikes = models.PositiveIntegerField(default=0)
    totlenewsarticles = models.PositiveIntegerField(default=0)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    email = models.EmailField(blank=True)
    rank_points = models.IntegerField(default=0,validators=[
       MinValueValidator(-8),
        MaxValueValidator(8)
    ])
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
    jioing_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

