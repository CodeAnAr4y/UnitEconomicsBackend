from django.urls import path
from .views import (
    ProductCreateAPIView,
    ProductListAPIView,
    ProductUpdateAPIView,
    ProductDeleteAPIView,  # импортируем новый эндпоинт
    SellerListAPIView,
    SellerCreateAPIView
)

urlpatterns = [
    path('products/add/', ProductCreateAPIView.as_view(), name='product-add'),
    path('products/all/', ProductListAPIView.as_view(), name='product-list'),
    path('products/update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product-update'),
    path('products/delete/<int:pk>/', ProductDeleteAPIView.as_view(), name='product-delete'),
    path('sellers/all/', SellerListAPIView.as_view(), name='seller-list'),
    path('sellers/add/', SellerCreateAPIView.as_view(), name='seller-add'),
]