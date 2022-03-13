from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET'])
def getData(request):
    my_dict = {'name': 'Petras', 'surname': 'Petraitis', 'from': 'big city'}
    return Response(my_dict)
