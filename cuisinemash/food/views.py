from django.shortcuts import render
from django.http import HttpResponse
from food.models import Dish
from random import randint
# Create your views here.

allDishes = Dish.objects.all()

def pickDish():
    dishId = randint(1,len(allDishes))
    dish = allDishes[dishId]
    return dish

def compareDishes(first, second):
    return first.id == second.id

def makeDishPair():
    match = True
    while match:
        firstDish = pickDish()
        secondDish = pickDish()
        if not (compareDishes(firstDish,secondDish)):
            match = False
            return firstDish, secondDish
        else:
            continue

def index(request):
    dishPair = makeDishPair()
    return HttpResponse("You should try eating %s %s"% dishPair[1], dishPair[2])