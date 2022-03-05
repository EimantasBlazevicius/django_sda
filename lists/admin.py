from django.contrib import admin
from .models import ToDoList, ToDoItems

# Register your models here.
admin.site.register(ToDoList)
admin.site.register(ToDoItems)
