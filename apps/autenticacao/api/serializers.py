from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from apps.autenticacao.models import Perfil, Plano


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    username = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )
    password = serializers.CharField(min_length=8)

    class Meta:
        model = User
        extra_kwargs = {'password': {'write_only': True}}
        fields = ('id', 'username', 'email', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
                                        validated_data['password'])
        return user


class PerfilSerializer(serializers.ModelSerializer):
    usuario = UserSerializer()

    class Meta:
        model = Perfil
        fields = ('id', 'usuario')


class PerfilSerializerSoft(serializers.ModelSerializer):

    class Meta:
        model = Perfil
        fields = ('id', 'usuario')


class PlanoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plano
        fields = ('id', 'nome')
