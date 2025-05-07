from django.contrib.auth.models import AbstractUser
from django.db import models

# Replacing GeeksModel with RRModel
class RRModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

# Custom user model
class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=100)
    mood = models.CharField(max_length=50, blank=True, null=True)
    motivation = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.email if self.email else self.username
