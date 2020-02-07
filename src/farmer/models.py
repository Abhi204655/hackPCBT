from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class Land(models.Model):
    length = models.IntegerField()
    width = models.IntegerField()
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField()
    city = models.TextField()
    state = models.TextField()
    image = models.ImageField(upload_to="land_img",null=True)
    

