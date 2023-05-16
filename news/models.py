from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="news")
    description = models.TextField()
    news_text = models.TextField()
    author = models.CharField(max_length=100)
    news_date = models.DateTimeField()
    publish_date = models.DateTimeField()
