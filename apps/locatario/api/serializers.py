from django.contrib.auth.models import User
from rest_framework import serializers, status
from rest_framework.response import Response

from apps.autenticacao.api.serializers import PerfilSerializer
from apps.autenticacao.models import Perfil
from apps.locatario.models import Locatario


class LocatarioSerializerSoft(serializers.ModelSerializer):
    class Meta:
        model = Locatario
        fields = (
            'nome', 'cpf', 'telefone', 'logradouro', 'numero', 'bairro',
            'cidade', 'estado', 'data_nasc', 'ativo', 'perfil'
        )


class LocatarioSerializer(serializers.ModelSerializer):
    perfil = PerfilSerializer()

    class Meta:
        model = Locatario
        fields = (
            'nome', 'cpf', 'telefone', 'logradouro', 'numero', 'bairro',
            'cidade', 'estado', 'data_nasc', 'ativo', 'perfil'
        )

    def create(self, validated_data):
        try:
            nome = validated_data['nome']
            cpf = validated_data['cpf']
            telefone = validated_data['telefone']
            logradouro = validated_data['logradouro']
            numero = validated_data['numero']
            bairro = validated_data['bairro']
            cidade = validated_data['cidade']
            estado = validated_data['estado']
            data_nasc = validated_data['data_nasc']

            perfil = validated_data['perfil']

            usuario = perfil['usuario']

            user = User.objects.create_user(usuario['username'], usuario['email'], usuario['password'])
            perfil = Perfil.objects.create(usuario=user)
            locatario = Locatario.objects.create(nome=nome, cpf=cpf, telefone=telefone, logradouro=logradouro,
                                                 numero=numero, bairro=bairro, cidade=cidade, estado=estado,
                                                 data_nasc=data_nasc, perfil=perfil)

            return locatario

        except Exception:
            return Response('Não foi possível efetuar o cadastro.', status.HTTP_400_BAD_REQUEST)
