from django.shortcuts import render
from recommender.models import Mood
import json
from django.http import HttpResponse


def index(request):
<<<<<<< HEAD
    '''sql = """
        SELECT id, name, categories FROM 
        ( SELECT *, ROW_NUMBER() 
         OVER (PARTITION BY categories) AS RowNo 
         FROM recommender_mood) AS rank 
         WHERE rank.RowNo<=5
    """
'''
    mood_names = ['1', '2']
    # mood_names = [m.name for m in Mood.objects.raw(sql)]
    # print('mood_names')
=======
    mood_names = [m.name for m in Mood.objects.order_by('?')[:50]]
>>>>>>> d089cceae20523321f5fac9227047965d0ae7b30
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
