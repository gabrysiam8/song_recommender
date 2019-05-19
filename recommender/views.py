from django.shortcuts import render
from recommender.models import Mood


def index(request):
    '''sql = """
        SELECT id, name, categories FROM 
        ( SELECT *, ROW_NUMBER() 
         OVER (PARTITION BY categories) AS RowNo 
         FROM recommender_mood) AS rank 
         WHERE rank.RowNo<=5
    """
'''
    mood_names = [m.name for m in Mood.objects.raw(sql)]
    print('mood_names')
    return render(request, 'index.html', {'moods': mood_names})
