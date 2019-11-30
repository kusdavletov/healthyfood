from django.db import models


class Program(models.Model):
    title = models.CharField(max_length=100)
    image = models.TextField()
    tag = models.TextField()
    target = models.TextField()
    aim = models.TextField()
    description = models.TextField()
    prohibition = models.TextField(blank=True)
    price_day = models.IntegerField()
    price_week = models.IntegerField()
    breakfast_info = models.TextField()
    breakfast_image = models.URLField()
    brunch_info = models.TextField()
    brunch_image = models.URLField()
    lunch_info = models.TextField()
    lunch_image = models.URLField()
    dunch_info = models.TextField()
    dunch_image = models.URLField()
    dinner_info = models.TextField()
    dinner_image = models.URLField()
