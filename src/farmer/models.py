from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class Land(models.Model):
    length = models.IntegerField(null=False)
    width = models.IntegerField(null=False)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    address = models.TextField(null=False)
    city = models.TextField(null=False)
    state = models.TextField(null=False)
    image = models.ImageField(upload_to="img/")