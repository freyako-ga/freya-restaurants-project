from django.db import models

# Create your models here.
class Review(models.Model):
    text = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    restaurant = models.ForeignKey(
        'restaurants.Restaurant', # syntax is appname.ModelName
        on_delete=models.CASCADE, # on_delete allows us to choose what happens to relations when a foreignKey is deleted. CASCADE tells psql to delete all relations
        related_name='reviews' # related_name allows us to name this relationship on the corresponding model
    )
    owner = models.ForeignKey(
        'jwt_auth.User',
        on_delete=models.CASCADE,
        related_name='reviews_created'
    )