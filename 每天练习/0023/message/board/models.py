from django.db import models

# Create your models here.


class Board(models.Model):
    name = models.CharField(max_length=10)
    content = models.CharField(max_length=100)
    date = models.DateTimeField()

    def __str__(self):
        return self.name