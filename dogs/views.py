from rest_framework.generics import ListAPIView,     RetrieveUpdateDestroyAPIView, CreateAPIView, DestroyAPIView, RetrieveAPIView
from .models import Dog, Favorite
from .serializers import DogSerializer, FavoriteSerializer
from .permissions import isOwnerOrReadyOnly
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class DogListView(ListAPIView):
    '''View for /dogs'''

    queryset = Dog.objects.all().order_by('name')
    serializer_class = DogSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class DogDetailView(RetrieveAPIView):

    '''view for one lonely dog'''

    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class FavoriteListView(CreateAPIView):
    ''' View for /dogs/id/favorites POST'''

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

class FavoriteDetailView(DestroyAPIView):
    ''' View for /dogs/id/favorites/favoriteId DELETE'''

    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    permission_classes = (isOwnerOrReadyOnly, )
