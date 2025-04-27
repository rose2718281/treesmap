from django.db import models


class Tree(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    planted_date = models.DateField()
    height = models.FloatField()
    health_status = models.CharField(max_length=50)

    def __str__(self):
        return self.name
