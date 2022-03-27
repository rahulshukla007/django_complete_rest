from cgitb import lookup
from codecs import lookup_error
from select import select
from django.http import Http404
from rest_framework import generics, mixins

from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Product
from .serializers import ProductSerializers
from products import serializers
from api.mixins import StaffEditorPermissionMixin

class ProductCreateAPIView(StaffEditorPermissionMixin, generics.CreateAPIView):
    queryset            = Product.objects.all()
    serializer_class    = ProductSerializers
   

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_create_view = ProductCreateAPIView.as_view()

class ProductListCreateAPIView(StaffEditorPermissionMixin, generics.ListCreateAPIView):
    queryset                    = Product.objects.all()
    serializer_class            = ProductSerializers  



    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()


#it is similar to the get request
class ProductDetailAPIView(StaffEditorPermissionMixin, generics.RetrieveAPIView):
    queryset            = Product.objects.all()
    serializer_class    = ProductSerializers

product_detail_view = ProductDetailAPIView.as_view()


class ProductListAPIView(StaffEditorPermissionMixin, generics.ListAPIView):
    queryset            = Product.objects.all()
    serializer_class    = ProductSerializers

product_list_view = ProductListAPIView.as_view()


@api_view(["GET", "POST"])
def product_alt_view(request, pk = None, *args, **kwargs):
    method = request.method

    if method == "GET": #pk is for getting single data
        if pk is not None:
            obj = get_object_or_404(Product, pk=pk) #if pk doesn't exist
            data = ProductSerializers(obj, many=False).data
            return Response(data)
        
        queryset = Product.objects.all()
        data = ProductSerializers(queryset, many=True).data
        return Response(data)

    if method == "POST":
        serializer = ProductSerializers( data = request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
    return Response({"invalid": "not good data"}, status=400)


class ProductUpdateAPIView(StaffEditorPermissionMixin, generics.UpdateAPIView):
    queryset            = Product.objects.all()
    serializer_class    = ProductSerializers
    lookup_field        = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(StaffEditorPermissionMixin, generics.DestroyAPIView):
    queryset            = Product.objects.all()
    serializer_class    = ProductSerializers
    lookup_field        = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

product_destroy_view = ProductDestroyAPIView.as_view()

class ProductListModelMixin(StaffEditorPermissionMixin, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.RetrieveModelMixin, generics.GenericAPIView):
    queryset            = Product.objects.all()
    serializer_class    = ProductSerializers
    lookup_field        = 'pk'  #this will work for retrieve model mixin



    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        print("serializer.validated_data", serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

product_list_model_mixin = ProductListModelMixin.as_view()