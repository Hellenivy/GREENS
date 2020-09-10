from django.urls import path
from .views import product_list
from .import views

urlpatterns = [
    path('products/', product_list, name='product-list'),
]