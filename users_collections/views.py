from rest_framework.viewsets import ModelViewSet
from .models import Collection
from .serializers import CollectionSerializer


class CollectionViewSet(ModelViewSet):
    queryset = Collection.objects.all()
    serializer_class = CollectionSerializer
