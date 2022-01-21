from rest_framework.generics import ListAPIView
from .models import Dog
from .serializers import DogSerializer

class DogListView(ListAPIView):
    '''View for /dogs'''

    queryset = Dog.objects.all().order_by('name')
    serializer_class = DogSerializer
