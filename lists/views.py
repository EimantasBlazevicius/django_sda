from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from .models import ToDoList

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class AllUserLists(LoginRequiredMixin, ListView):
    model=ToDoList
    template_name='home.html'
    
    def get_queryset(self):
        return ToDoList.objects.filter(user=self.request.user)

def list(request, id):
    list = ToDoList.objects.get(id=id)
    if request.method == "POST":
        print(request.POST)

        if request.POST.get('save'):
            checked = request.POST.getlist('checkbox')
            for item in list.todoitems_set.all():
                if str(item.id) in checked:
                    item.isCompleted = True
                else:
                    item.isCompleted = False
                item.save()
        elif request.POST.get('add'):
            text = request.POST.get('new')
            if len(text) > 3:
                list.todoitems_set.create(text=text, isCompleted=False)
            else:
                print("Užduoties tekstas per trumpas")
        elif request.POST.get('delete'):
            id_to_delete = request.POST.get('delete')
            for item in list.todoitems_set.all():
                if str(item.id) == id_to_delete:
                    item.delete()
        return redirect('list', id=id)
    else:
        context = {"title":f"{list.title}","items": list.todoitems_set.all() }
        return render(request, 'index.html', context=context)
