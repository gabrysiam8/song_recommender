import os
from glob import glob

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'song_recommender.settings')

import django
django.setup()

from recommender.models import Mood


def save_moods_from_file(filepath):
    categories = os.path.basename(filepath).split('.')[0].split('_')
    with open(filepath, 'r') as file:
        moods = [mood.strip() for mood in file.read().split(',')]
        for mood_name in moods:
            mood = Mood()
            mood.name = mood_name
            mood.categories = categories
            mood.save()


if __name__ == "__main__":

    for filepath in glob('data/keywords/*.txt'):
        print('Reading from file ' + filepath)
        save_moods_from_file(filepath)
