from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField("title", max_length=200)
    slug = models.SlugField("slug", unique=True)
    description = models.CharField("description", max_length=100, blank='True')
    content = models.TextField("content")
    create_date = models.DateTimeField("create_date", auto_now_add=True)
    modify_date = models.DateTimeField("modify_date", auto_now=True)