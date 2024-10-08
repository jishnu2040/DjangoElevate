from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio  = models.CharField(blank=True, max_length=100)

    def __str__(self):
        return f'{self.user.username} Profile'
        
class Car(models.Model):
    name = models.CharField(max_length=50)
    
