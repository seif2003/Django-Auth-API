from django.urls import path
from .views import UserRegisterView, CustomAuthToken

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', CustomAuthToken.as_view(), name='login'),
]