from django.db import models

#user imports
from django.utils.timezone import now

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField(default=now)