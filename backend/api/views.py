from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    """
    Django Rest Framework View
    """
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        # #Build the dictionary manually from the model
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.content
        # data['price'] = model_data.price
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return Response(data)