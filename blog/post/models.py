from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=256)
    body = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    insert_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "\n" + self.title + ":\n" + self.body + "\n"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(default=0)
    insert_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.body
