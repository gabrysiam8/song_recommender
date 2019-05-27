from django.shortcuts import render
from recommender.models import Mood


def index(request):
    mood_names = [m.name for m in Mood.objects.order_by('?')[:50]]
    return render(request, 'index.html', {'moods': mood_names})
