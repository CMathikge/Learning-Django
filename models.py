from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Models):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    bio= models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_picture/',blank=True)
    
    def str (self):
        return self.user.username
    
    
    
    