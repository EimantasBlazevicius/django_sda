from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

# Create your views here.
@csrf_protect
def register(request):
    return render(request, 'registration/register.html')