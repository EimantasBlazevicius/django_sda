from django.shortcuts import render, redirect
from .models import ToDoList

# Create your views here.
def index(request):
    list = ToDoList.objects.get(id=1)
    if request.method == "POST":
        print(request.POST)
        checked = request.POST.getlist('checkbox')
        for item in list.todoitems_set.all():
            if str(item.id) in checked:
                item.isCompleted = True
            else:
                item.isCompleted = False
            item.save()
        return redirect('index')
    else:
        context = {"title":f"{list.title}","items": list.todoitems_set.all() }
        return render(request, 'index.html', context=context)
