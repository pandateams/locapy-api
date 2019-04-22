from django.core.validators import RegexValidator
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from apps.autenticacao.api.serializers import PerfilSerializer
from apps.autenticacao.models import Perfil
from apps.autenticacao.models import User
from apps.email.logica import envia_email_bemvindo
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
            RegexValidator(regex="([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")
        ]
    )

    class Meta:
        model = Locador
        fields = (
            'id', 'nome_fantasia', 'razao_social', 'inscricao_estadual', 'cnpj', 'endereco', 'telefone',
            'perfil')

    def create(self, validated_data):
        try:
            nome_fantasia = validated_data['nome_fantasia']
            razao_social = validated_data['razao_social']
            inscricao_estadual = validated_data['inscricao_estadual']
            cnpj = validated_data['cnpj']
            endereco = validated_data['endereco']
            telefone = validated_data['telefone']
            perfil = validated_data['perfil']

            usuario = perfil['usuario']

            user = User.objects.create_user(usuario['username'], usuario['email'], usuario['password'])
            perfil = Perfil.objects.create(usuario=user)
            locador = Locador.objects.create(nome_fantasia=nome_fantasia, razao_social=razao_social,
                                             inscricao_estadual=inscricao_estadual, cnpj=cnpj, endereco=endereco,
                                             telefone=telefone, perfil=perfil)

            serializer = LocadorSerializer(locador)
            envia_email_bemvindo(serializer.data)
            return Response(serializer.data, status.HTTP_201_CREATED)

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
            RegexValidator(regex="([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})")
        ]
    )

    class Meta:
        model = Locador
        fields = ('id', 'nome_fantasia', 'razao_social', 'inscricao_estadual', 'cnpj', 'endereco', 'telefone',
                  'perfil')
