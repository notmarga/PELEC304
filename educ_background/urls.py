from django.urls import path
from . import views

urlpatterns = [
    path('elementary/', views.elementary_view, name='elementary'),
    path('highschool/', views.highschool_view, name='highschool'),
    path('seniorhigh/', views.seniorhigh_view, name='seniorhigh'),
]