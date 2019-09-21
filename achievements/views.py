from django.shortcuts import render, get_object_or_404
from .models import Achievement


def home(request):
    achievements = Achievement.objects
    return render(request, 'achievement/home.html', {'achievements': achievements})


def detail(request, achievement_id):
    achievement_detail = get_object_or_404(Achievement, pk=achievement_id)
    return render(request, 'achievement/detail.html', {'achievement': achievement_detail})
