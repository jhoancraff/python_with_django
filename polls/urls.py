
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/detail/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/resultado/', views.ResulatadoView.as_view(), name='resultado'),
    path('<int:question_id>/votos/erer/', views.votos, name='votos'),
    

]
