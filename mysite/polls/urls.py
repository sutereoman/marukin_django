from django.urls import path
from . import views
 
urlpatterns = [
    path('template/', views.index_template, name='index_template'),
    path('map/', views.map_template, name='map_template'),

]