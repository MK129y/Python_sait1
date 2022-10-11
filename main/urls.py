from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home5'),
    path('about5', views.about, name='about5'),
    path('create5', views.about, name='create5'),
    path('about1', views.about, name='about1'),
               ]