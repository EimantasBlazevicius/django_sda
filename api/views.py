from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ToDoListSerializer
from lists.models import ToDoList
from django.http import Http404
from rest_framework import status

# Create your views here.
class ToDoListList(APIView):
    """
    List all TodoLists, or create a new list.
    """
    def get(self, request, format=None):
        data = ToDoList.objects.all()
        serializer = ToDoListSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ToDoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)