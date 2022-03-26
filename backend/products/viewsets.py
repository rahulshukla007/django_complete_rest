from cgitb import lookup
from rest_framework import mixins,viewsets

from .models import Product
from .serializers import ProductSerializers

class ProductViewSet(viewsets.ModelViewSet):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'

class ProductGenericViewset(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    queryset  = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'
