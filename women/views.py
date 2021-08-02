from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
def index(request):
    return HttpResponse("Страница приложения women")

def categories(request, cat):
    print(request.GET)
    return HttpResponse(f'<h1>Статьи по категориям: {cat}</h1>')

def archive(request, year):
    if int(year) > 2021:
        # raise Http404()  #Генерация исключения 404
        # return redirect('/')
        return redirect("home")
    return HttpResponse(f'<h1>Архив по годам: </h1><p>{year}</p>')

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')