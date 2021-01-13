from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class InfoPage(models.Model):
    info = models.TextField()
    tel = models.CharField(max_length=20, blank=True)

# Create your models here.
class Picture(models.Model):
    image = CloudinaryField('image',folder="sunojan-saha")
