import imp
from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('<int:pk>/', views.ProductDetailAPIView.as_view())
]