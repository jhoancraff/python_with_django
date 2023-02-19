import datetime
from pyexpat import model

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    quiestion_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self) -> str:
        return self.quiestion_text
    
    def was_plublished_recently(self):
        return  timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.choice_text  

class Nombre(models.Model):
    name = models.CharField(max_length=200)


    def __str__(self): 
        return self.name

class respuesta(models.Model):
    pregunta = models.ForeignKey(Nombre, on_delete=models.CASCADE)
    elegir = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.elegir    

