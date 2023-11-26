from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate

User = get_user_model()




class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="cet adresse mail est déjà utilisée"
            )
        ]
    )

    class Meta:
        model = User
        fields = ('email', 'password', 'location', 'first_name', 'last_name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class AuthTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        user = authenticate(request=self.context.get('request'),
                            username=attrs.get('email'),
                            password=attrs.get('password'))

        if not user:
            msg = "Erreur : L'email ou le mot de passe est incorrect."
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


