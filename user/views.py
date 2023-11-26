from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from .serializers import UserSerializer, AuthTokenSerializer
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import ValidationError


User = get_user_model()



class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        response.status_code = status.HTTP_201_CREATED
        response.data = {
            'message': 'utilisateur créé avec succès'
        }
        return response



class CustomAuthToken(ObtainAuthToken):
    serializer_class = AuthTokenSerializer  

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data=request.data,context={'request': request})
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            raise ValidationError({'message': e.detail['non_field_errors']})
        user = serializer.validated_data['user']

        # Delete existing tokens for the user
        Token.objects.filter(user=user).delete()

        # Create a new token for the user
        token = Token.objects.create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'location': user.location,
            'first_name': user.first_name,
            'last_name': user.last_name
        })
