from django.shortcuts import render
from django.http import HttpResponse
import random
from datetime import datetime

def about(request):
    return HttpResponse("Меня зовут Абдымиталийп. Я изучаю Django 🚀")

def current_time(request):
    now = datetime.now().time()

    if now < datetime.strptime("12:00", "%H:%M").time():
        message = "Сейчас утро 🌅"
    elif datetime.strptime("12:00", "%H:%M").time() <= now <= datetime.strptime("14:00", "%H:%M").time():
        message = "Сейчас обед 🍽️"
    elif datetime.strptime("15:00", "%H:%M").time() <= now <= datetime.strptime("20:00", "%H:%M").time():
        message = "Сейчас вечер 🌇"
    else:
        message = "Сейчас ночь 🌙"

    return HttpResponse(message)

def quotes(request):
    quotes_list = [
        "Не ошибается тот, кто ничего не делает. — Л.Н. Толстой",
        "Чтобы быть незаменимым, нужно всё время меняться. — Коко Шанель",
        "Мы то, что мы думаем. — Будда",
        "Счастье — это когда мысли, слова и дела совпадают. — Ганди",
        "Жизнь — это то, что происходит, пока ты строишь планы. — Джон Леннон",
    ]
    return HttpResponse(random.choice(quotes_list))