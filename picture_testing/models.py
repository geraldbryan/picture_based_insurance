from django.db import models
from django.db import models
from django.db.models.deletion import CASCADE
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=CASCADE)
    name = models.CharField(max_length=250, null=True)
    farmer_id = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return f'{self.user.username} Profile'

class Image(models.Model):
    image = models.ImageField(upload_to ='Image/')