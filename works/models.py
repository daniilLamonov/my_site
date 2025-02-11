from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User

class Work(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    reference = models.URLField(max_length=200, blank=True)

    class Meta:
        ordering = ['-publish']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('work_detail', args=[self.slug])


class WorkImage(models.Model):
    work = models.ForeignKey(Work, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="work_images/")

    def __str__(self):
        return f"Image for {self.work.title}"
