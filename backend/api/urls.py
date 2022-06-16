from django.urls import path

from . import views #, include

urlpatterns = [
    path('', views.api_home) #localhost:8000/api
    #could add api urls here
    #path('products/', include('products.urls))
]