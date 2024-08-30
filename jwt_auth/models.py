from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=50, unique=True)
    profile_image=models.URLField(
        default ='https://res.cloudinary.com/dycdgsbm3/image/upload/v1724406847/person-placeholder-5_pttwjo.png'
    )
