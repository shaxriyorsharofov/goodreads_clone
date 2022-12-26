from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    profile_picture = models.ImageField(default='profil_default_img.png', upload_to='profile/')


