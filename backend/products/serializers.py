from turtle import tilt, title
from urllib import request
from wsgiref.validate import validator
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from . import validators

class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only = True)
    edit_url = serializers.SerializerMethodField(read_only = True)
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field="pk")

    title = serializers.CharField(validators=[validators.unique_product_title, validators.validate_title_solar])
    # name = serializers.CharField(source='title', read_only = True)
    class Meta:
        model = Product
        fields = [
            "url",
            'edit_url',
            'pk',
            'title',
            # 'name',
            'content',
            'price',
            'sale_price',
            'my_discount'
            ]

    # def validate_title(self, value):
    #     qs = Product.objects.filter(title__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name")
    #     return value

    def get_edit_url(self, obj):
        #return f"/api/products/li/{obj.pk}/"
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk":obj.pk} , request=request)

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
      

