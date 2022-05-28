from django.urls import path
from . import views
 
urlpatterns = [
    path('template/', views.index_template, name='index_template'),
    path('menu/', views.menu_template, name='menu_template'),
    path('map/', views.map_template, name='map_template'),
    path('gallery/', views.gallery_template, name='gallery_template'),

]