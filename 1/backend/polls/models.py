from django.db import models

#user imports
from django.utils.timezone import now

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField(default=now)

    def __str__(self):
        return self.question_text
    


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ha törlünk egy kerdest akkor a hozza kapcsolodo valasz is torlodni fog (erre jo a cascade)
    choice_text = models.CharField(max_length=200)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text+" ("+self.question.question_text+")" # a kerdes kiirasa a valasztasi lehetoseg utan
    
    

