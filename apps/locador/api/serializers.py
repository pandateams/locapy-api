from django.core.validators import RegexValidator
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from apps.autenticacao.api.serializers import PerfilSerializer
from apps.autenticacao.models import User, Perfil
from apps.locador.models import Locador


class LocadorSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()

    cnpj = serializers.RegexField(
        regex="([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})",
        required=True,
        max_length=14,
        min_length=14,
        allow_blank=False,
        validators=[
            UniqueValidator(queryset=Locador.objects.all()),
            RegexValidator(
                regex="([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")
        ]
    )

    class Meta:
        model = Locador
        fields = (
            'id', 'nome_fantasia', 'razao_social', 'inscricao_estadual', 'cnpj', 'endereco', 'telefone',
            'perfil')

    def create(self, validated_data):
        try:
            payload = {
                'nome_fantasia': validated_data['nome_fantasia'],
                'razao_social': validated_data['razao_social'],
                'inscricao_estadual': validated_data['inscricao_estadual'],
                'cnpj': validated_data['cnpj'],
                'endereco': validated_data['endereco'],
                'telefone': validated_data['telefone'],
                'perfil': validated_data['perfil'],
                'usuario': validated_data['perfil']['usuario']
            }

            user = User.objects.create_user(payload['usuario']['username'], payload['usuario']['email'],
                                            payload['usuario']['password'])
            perfil = Perfil.objects.create(usuario=user)
            locador = Locador.objects.create(nome_fantasia=payload['nome_fantasia'],
                                             razao_social=payload['razao_social'],
                                             inscricao_estadual=payload['inscricao_estadual'], cnpj=payload['cnpj'],
                                             endereco=payload['endereco'],
                                             telefone=payload['telefone'], perfil=perfil)

            return locador

        except Exception:
            return Response('Não foi possível efetuar o cadastro.', status.HTTP_400_BAD_REQUEST)


class LocadorSerializerSoft(serializers.ModelSerializer):
    cnpj = serializers.RegexField(
        regex="([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})",
        required=True,
        max_length=14,
        min_length=14,
        allow_blank=False,
        validators=[
            UniqueValidator(queryset=Locador.objects.all()),
            RegexValidator(
                regex="([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")
        ]
    )

    class Meta:
        model = Locador
        fields = ('id', 'nome_fantasia', 'razao_social', 'inscricao_estadual', 'cnpj', 'endereco', 'telefone',
                  'perfil')
