from django.db import models

# Create your models here.

class Screening(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField()
    director = models.CharField(max_length=200)
    actors = models.TextField()
    producer = models.CharField(max_length=200)
    production_date = models.DateTimeField()
    release_date = models.DateTimeField()
    create_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(auto_now=True)
    
