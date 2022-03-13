from django.urls import path, include

from . import views

urlpatterns = [
    # path('register/', views.register, name='register')
    path('', views.ToDoListList.as_view(), name='todo_lists')
]
