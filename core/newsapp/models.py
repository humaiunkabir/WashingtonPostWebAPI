from django.db import models

# Create your models here.
class NewsPost(models.Model):
    title = models.TextField()
    content = models.TextField()
    images = models.TextField()

