from django.db import models
from django.contrib import admin


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.IntegerField(default=100)

    def __str__(self):
        return self.name
