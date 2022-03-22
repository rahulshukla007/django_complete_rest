from django.http import JsonResponse
import json
from products.models import Product
from django.forms import model_to_dict

from rest_framework.decorators import api_view
from rest_framework.response import Response
from products.serializers import ProductSerializers

from django.http import JsonResponse

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    #now our data is validate through serializer
    serializer = ProductSerializers( data = request.data)
    if serializer.is_valid(raise_exception=True):
        instance = serializer.save() #this line create an instance
        print("instance", instance)
        data = serializer.data
        return Response(data)
    return Response({"invalid": "not good data"}, status=400)


# @api_view(["GET"])
# def api_home(request, *args, **kwargs):
#     """
#     DRF API View
#     """
#     #order by question marks take the random order
#     instance = Product.objects.all().order_by("?").first()
#     data = {}
#     if instance:
#         ## data['id'] = model_data.id
#         ## data['title'] = model_data.title
#         ## data['content'] = model_data.content
#         ## data['price'] = model_data.price

#         # saves time to write the above 4 lines
#         data = ProductSerializers(instance).data
#     return Response(data)



# def api_home(request, *args, **kwargs):
#     print(request.GET) #get url query parameter

#     body = request.body #byte string of json data
#     data = {}
#     try:
#         data = json.loads(body) #convert json string to python dictionary
#     except:
#         pass
#     data['params']          = dict(request.GET)
#     data['headers']         = dict(request.headers)
#     data['content_type']    = request.content_type
#     return JsonResponse(data)

