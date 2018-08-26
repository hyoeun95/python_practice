from django.db import models

# Create your models here.

class Post(models.Model):    
    title = models.CharField("title", max_length=200)
    slug = models.SlugField("slug", unique=True)
    description = models.CharField("description", max_length=100, blank='True')
    content = models.TextField("content")
    create_date = models.DateTimeField("create_date", auto_now_add=True)
    modify_date = models.DateTimeField("modify_date", auto_now=True)

def __str__(self):
    return self.title

class Comment(models.Model):
    post = models.ForeignKey('community.Post', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text