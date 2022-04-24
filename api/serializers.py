from rest_framework import serializers
from lists.models import ToDoList, ToDoItems


class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'
 