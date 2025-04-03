from django.shortcuts import render
from app_dj.models import Articles

def home(request):
    articles = Articles.objects.all()
    return render(request, "app_dj/home.html", {"articles": articles})

