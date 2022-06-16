from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
    """
    Django Rest Framework API View
    """
    instance = Product.objects.all().order_by("?").first()
    """
    In a GET request, data needs to be a DICT as it is similar to JSON
    In a POST request, we want the data sent to us
    """
    # data = {}
    serializer = ProductSerializer(data=request.data) #Gets instance of ProductSerializer class and returns data
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        # data = model_to_dict(instance, fields=['id', 'title', 'price'])
        return Response(serializer.data)
    return Response({"invalid": "not good data"}, status=400)