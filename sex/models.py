from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Blogger(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
