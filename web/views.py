from django.shortcuts import render, get_object_or_404
from .models import News


def index(request):
    return render(request, 'ulumi/index.html')


def news_detail(request):
    news = News.objects.all()
    return render(request, 'ulumi/news.html', {'news':news})

def history(request):
    return render(request,'ulumi/history.html')


def full_detail(request, year, month, day, news):
    news = get_object_or_404(News,
                        slug=news,
                        written__year = year,
                        written__month = month, 
                        written__day = day)
    return render(request, 'ulumi/full_detail.html', {'news':news})