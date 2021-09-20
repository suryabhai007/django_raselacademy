from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Blog(models.Model):
    title = models.CharField(max_length=100)
    heading = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField()
    category = models.ManyToManyField(Category, related_name="blog")

    def get_absolute_url(self):
        return reverse("LatestBlogsFeed")

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=100)
    body = models.TextField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name="comment", blank=True)



