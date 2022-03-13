from django.urls import path

from . import views

urlpatterns = [
    path('', views.ToDoListList.as_view(), name='todo_lists'),
    path('<int:pk>', views.ToDoListDetail.as_view(), name='todo_list_detail')
]
