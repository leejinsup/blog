from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    title = models.CharField(max_length=500)
    contents = models.TextField()
    hits = models.IntegerField(default=0)

    def __str__(self):
        return self.title