from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(blank=True, null=True)
    def __str__(self):
        return self.title

class Works(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='work_images/', default='work_images/default.png')
    reference = models.URLField(max_length=200)
    date_posted = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.title