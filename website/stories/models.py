from django.db import models

class Author(models.Model):
    first_name    = models.CharField(max_length=50)
    last_name     = models.CharField(max_length=50)
    email_address = models.EmailField()
    insert_date   = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Story(models.Model):
    title       = models.CharField(max_length=255)
    synopsis    = models.CharField(max_length=255)
    body        = models.TextField()
    author      = models.ForeignKey(Author, on_delete=models.CASCADE)
    insert_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

