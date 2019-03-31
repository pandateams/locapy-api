from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.response import Response

from apps.autenticacao.api.serializers import PerfilSerializer, PlanoSerializer
from apps.autenticacao.models import Perfil
from apps.locador.models import Locador


class LocadorSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()
    plano = PlanoSerializer()

    class Meta:
        model = Locador
        fields = (
            'id', 'nome_fantasia', 'razao_social', 'inscricao_estadual', 'cnpj', 'endereco', 'telefone', 'plano',
            'perfil')

    def create(self, validated_data):
        try:
            nome_fantasia = validated_data['nome_fantasia']
            cnpj = validated_data['cnpj']

            perfil = validated_data['perfil']

            usuario = perfil['usuario']

            user = User.objects.create_user(usuario['username'], usuario['email'], usuario['password'])
            perfil = Perfil.objects.create(usuario=user)
            locador = Locador.objects.create(nome_fantasia=nome_fantasia, cnpj=cnpj, perfil=perfil)

            return locador

        except Exception:
            return Response('Não foi possível efetuar o cadastro.', status.HTTP_400_BAD_REQUEST)


class LocadorSerializerSoft(serializers.ModelSerializer):
    class Meta:
        model = Locador
        fields = ('id', 'nome_fantasia', 'razao_social', 'inscricao_estadual', 'cnpj', 'endereco', 'telefone', 'plano',
                  'perfil')
