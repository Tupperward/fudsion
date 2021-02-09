from django.urls import path
from . import views
urlpatterns = [
    path('food/', views.food, name='food'),
    path('suggestions/',views.suggestions, name='suggestions'),
    path('', views.index, name='index'),
]