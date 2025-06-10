from django.db import models
from django.conf import settings

# Create your models here.
class Image(models.Model):
  title = models.CharField(max_length=100)
  imageURL = models.ImageField(upload_to="images/")
  uploaded = models.DateField(auto_now=True)
  private = models.BooleanField(default=False)
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  
  def __str__(self):
    return self.title