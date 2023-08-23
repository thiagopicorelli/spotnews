from django.shortcuts import render
from news.models import News


def index(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)

def news_details(request, id):
    context = {"news": News.objects.get(id=id)}
    context["news"].categoriesList = context["news"].categories.all()
    return render(request, 'news_details.html', context)

def categories_form(request):
    return render(request, 'categories_form.html')