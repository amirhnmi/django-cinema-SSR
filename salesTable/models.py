from django.db import models

# Create your models here.

class SalesTable(models.Model):
    movie_name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    image = models.ImageField(upload_to="salestable")
    price = models.IntegerField()
    last_update = models.DateTimeField()