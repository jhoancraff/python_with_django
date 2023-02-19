import datetime
from urllib import response

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse  

from .models import Question, Choice
# Create your tests here.

class QuestionModelTexts(TestCase):
    
    def test_preguntas_del_pasado(self):
        """pregunta del pasado"""
        tiempo = timezone.now() + datetime.timedelta(days=30)
        pregunta = Question(quiestion_text='¿Porque platzi es lo mejor?', pub_date=tiempo)
        self.assertIs(pregunta.was_plublished_recently(), False) 
    
    def test_was_published_recently_with_future_question(self):
        """was_published_recently returns false for questions whose pub_date is in future""" 

        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question( quiestion_text='¿Quiesn es el mejor director de curso de platzi?' , pub_date=time)
        self.assertIs(future_question.was_plublished_recently(), False)

#def create_question(quiestion_text, days):
    #tiempo = timezone.now() + datetime.timedelta(days=30)
    #return Question.objects.create(quiestion_text=quiestion_text, pub_date=days)
class QuestionTextIndex(TestCase):

    def test_if_no_question(self):
        """if no question, return messaje error_mensaje"""
        respose = self.client.get(reverse("polls:index"))   
        self.assertEqual(respose.status_code, 200)
        self.assertContains(respose, "No polls are availed")
        self.assertQuerysetEqual(respose.context["lates_quiestion_list"], [])  

    def test_question_for_future(self):

        time = timezone.now() + datetime.timedelta(days=30)
        return Question.objects.create(quiestion_text='futura pregunta', pub_date=time)
        
        
               
    
       