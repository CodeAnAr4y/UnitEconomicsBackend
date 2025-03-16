from django.urls import path
from .views import ProductCreateAPIView, ProductListAPIView, SellerListAPIView, SellerCreateAPIView

urlpatterns = [
    path('products/add/', ProductCreateAPIView.as_view(), name='product-add'),
    path('products/all/', ProductListAPIView.as_view(), name='product-list'),
    path('sellers/all/', SellerListAPIView.as_view(), name='seller-list'),
    path('sellers/add/', SellerCreateAPIView.as_view(), name='seller-list'),
]
