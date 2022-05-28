from django.shortcuts import render

# Create your views here.
def index_template(request):
    return render(request, 'index.html')

def menu_template(request):
    return render(request, 'menu.html')

def map_template(request):
    return render(request, 'map.html')

def gallery_template(request):
    return render(request, 'gallery.html')