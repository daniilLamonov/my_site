from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.
class Work(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    image = models.ImageField(upload_to='work_images/', default='work_images/default.png')
    reference = models.URLField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ['-publish']
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('work_detail', args=[self.slug])
