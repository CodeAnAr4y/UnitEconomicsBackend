from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Product, Seller
from .serializers import ProductSerializer, SellerSerializer


@method_decorator(csrf_exempt, name='dispatch')
class ProductCreateAPIView(APIView):
    """
    Эндпоинт для создания нового товара.
    Ожидает POST-запрос с данными:
    {
        "marketplace": "OZON" или "Wildberries",
        "details": {
            "название": "Товар 1",
            "цена": "100",
            "описание": "Описание товара"
         }
    }
    Поле manager не передаётся в запросе, оно автоматически устанавливается как текущий пользователь.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            # При сохранении передаём текущего пользователя как manager
            serializer.save(manager=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductListAPIView(APIView):
    """
    Эндпоинт для получения списка товаров.
    Если используется роль менеджера, возвращает только товары, привязанные к текущему пользователю.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # Фильтрация списка товаров по текущему менеджеру
        products = Product.objects.filter(manager=request.user)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@method_decorator(csrf_exempt, name='dispatch')
class SellerCreateAPIView(APIView):
    """
    Эндпоинт для создания нового продавца.
    Ожидает POST-запрос с данными:
    {
        "name": "Название продавца"
    }
    Поле manager не передаётся в запросе, оно автоматически устанавливается как текущий пользователь.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = SellerSerializer(data=request.data)
        if serializer.is_valid():
            # Перед сохранением устанавливаем текущего пользователя в качестве менеджера продавца
            serializer.save(manager=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SellerListAPIView(APIView):
    """
    Эндпоинт для получения списка продавцов.
    Если используется роль менеджера, возвращает только продавцов, закреплённых за текущим пользователем.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        sellers = Seller.objects.filter(manager=request.user)
        serializer = SellerSerializer(sellers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)