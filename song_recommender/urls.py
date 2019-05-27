from django.contrib import admin
from django.urls import path
from recommender import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/get_moods', views.get_moods, name='get_moods')
]
