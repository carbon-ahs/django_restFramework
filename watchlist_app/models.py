from django.db import models
from django.utils.translation import activate

class Movie(models.Model):
    name = models.CharField(max_length = 50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name 