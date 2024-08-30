from django.db import models
from django.contrib.postgres.fields import ArrayField


class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    cuisines = models.ManyToManyField(
        'cuisines.Cuisine',
        related_name='restaurants',
        blank=True
    )
    description = models.TextField(max_length=1000)
    owner = models.ForeignKey(
        'jwt_auth.User',
        on_delete=models.CASCADE,
        related_name='restaurants_created',
        )
    
    def __str__(self):
        return f'{self.name} - {self.location})'

