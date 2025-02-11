from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)
# Create your models here.
class Post(models.Model):
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=200)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    objects = models.Manager()
    published = PublishedManager()
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['publish']),
        ]
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])
