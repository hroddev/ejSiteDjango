from django.db import models

class Directors(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    
class Movies(models.Model):
    name = models.CharField(max_length=100)
    directors = models.ManyToManyField(Directors, related_name="movies")
    year = models.IntegerField(blank=True, null=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

