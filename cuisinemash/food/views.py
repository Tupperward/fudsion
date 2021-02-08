from django.shortcuts import render
from django.http import HttpResponse, Http404
from food.models import Dish
from random import randint
from django.template import loader

# Create your views here.

allDishes = Dish.objects.all()

def pickDish():
    dishId = randint(0,len(allDishes)-1)
    return allDishes[dishId]

def compareDishes(first, second):
    return first.id == second.id

def compareCuisine(first,second):
    return first.cuisine == second.cuisine

def makeDishPair():
    match = True
    while match:
        firstDish = pickDish()
        secondDish = pickDish()
        if not (compareDishes(firstDish,secondDish)) and not (compareCuisine(firstDish,secondDish)):
            match = False
            return firstDish, secondDish
        else:
            continue

def index(request):
    try:
        dishPair = makeDishPair()
    except:
        raise Http404("Page does not exist")
    context = {'dishPair': dishPair}
    return render(request, 'food/index.html', context)


def suggestions(request):
    response = "Here's where you submit suggestions for food to go into this bullshit app."
    return HttpResponse(response)