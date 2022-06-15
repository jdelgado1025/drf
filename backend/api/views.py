import json
import re
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    print(request.GET)
    body = request.body
    data = {}
    try:
        data = json.loads(body) #takes string of JSON and converts to python Dict
    except:
        pass
    print(data)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)