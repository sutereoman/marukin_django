from django.shortcuts import render

# Create your views here.
def index_template(request):
    return render(request, 'index.html')

def map_template(request):
    return render(request, 'map.html')