from django.db import models
from django.urls import reverse
from django.conf import settings


class Post(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    hero_image = models.ImageField(upload_to="uploads", null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
