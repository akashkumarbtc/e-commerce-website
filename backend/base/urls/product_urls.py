from django.urls import path
from ..views import product_views as views

urlpatterns = [
    path('', views.get_products, name="products"),
    path('<str:pk>/', views.get_product, name="product"),
]