from django.shortcuts import render
from recommender.models import Mood
import json
from django.http import HttpResponse
from .suggestions import find_song_suggestions


def index(request):
    mood_names = [m.name for m in Mood.objects.order_by('?')[:50]]
    return render(request, 'index.html', {'moods': mood_names})


def get_moods(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        moods = Mood.objects.filter(name__startswith=q)[:20]
        results = []
        for mood in moods:
            mood_json = {}
            mood_json['id'] = mood.id
            mood_json['label'] = mood.name
            mood_json['value'] = mood.name
            results.append(mood_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def search_song(request):
    moods = request.POST.getlist('moods[]')
    matched_song = find_song_suggestions(moods)
    data = json.dumps(matched_song)
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
