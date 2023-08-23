from django.shortcuts import render, redirect
from news.models import News, Categories
from news.forms import CreateCategoryForm


def index(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)

def news_details(request, id):
    context = {"news": News.objects.get(id=id)}
    context["news"].categoriesList = context["news"].categories.all()
    return render(request, 'news_details.html', context)

def categories_form(request):
    form = CreateCategoryForm()
    if request.method == "POST":
        form = CreateCategoryForm(request.POST)
        if form.is_valid():
            Categories.objects.create(**form.cleaned_data)
            return redirect("home-page")
    context = {"form": form}
    return render(request, 'categories_form.html', context)

def news_form(request):
    return render(request, "news_form.html")
    