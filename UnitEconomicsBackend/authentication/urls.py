from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import RegisterView, LoginView, LogoutView, UserProfileView  

urlpatterns = [  
    path('register/', RegisterView.as_view(), name='register'),  
    path('login/', LoginView.as_view(), name='login'),  
    path('logout/', LogoutView.as_view(), name='logout'), 
    path('profile/', UserProfileView.as_view(), name='user-profile'),
]