from django.shortcuts import render

# Create your views here.
def index(request):
    context = {"name": "Petras"}
    return render(request, 'index.html', context=context)
