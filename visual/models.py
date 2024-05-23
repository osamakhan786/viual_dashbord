from django.db import models

# Create your models here.
class Visaul(models.Model):
    end_year = models.CharField(max_length=10)
    intensity = models.CharField(max_length=10)
    sector = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    url = models.CharField(max_length=200)
    region = models.CharField(max_length=100)
    start_year = models.CharField(max_length=100)
    added = models.CharField(max_length=100)
    published = models.CharField(max_length=300)
    country = models.CharField(max_length=300)
    relevance = models.CharField(max_length=10)
    pestle = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    title = models.CharField(max_length=500)
    likelihood = models.CharField(max_length=100)