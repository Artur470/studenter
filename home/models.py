from django.db import models


class BlogM(models.Model):
    name = models.CharField(max_length=10)
    surname = models.CharField(max_length=15)
    course = models.IntegerField()

    def __str__(self):
        return f'{self.pk}  {self.name}'