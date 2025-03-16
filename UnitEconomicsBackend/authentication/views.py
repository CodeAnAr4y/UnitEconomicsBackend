from rest_framework import generics, status  
from rest_framework.response import Response  
from django.contrib.auth.models import User  
from rest_framework.permissions import AllowAny, IsAuthenticated  
from .serializers import UserSerializer, LoginSerializer, RegisterSerializer  
from django.contrib.auth import login, logout

class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        """
        Переопределяем метод create, чтобы после успешной регистрации
        выполнить автоматический логин пользователя.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        # Автоматический вход пользователя после регистрации
        login(request, user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class UserProfileView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        # Для отладки: можно вывести в лог данные пользователя
        print(f"Current user: {request.user}")
        user = request.user
        if user.is_authenticated:
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'detail': 'Authentication credentials were not provided.'},
                        status=status.HTTP_403_FORBIDDEN)

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        # Логиним пользователя, используя session-based аутентификацию
        login(request, user)
        return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)

class LogoutView(generics.GenericAPIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        logout(request)
        return Response({'message': 'Logout successful'}, status=status.HTTP_200_OK)