from rest_framework import serializers

from apps.sala.models import Sala, Recurso, TipoRecurso, Galeria


class SalaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sala
        fields = (
            'id', 'nome', 'metragem', 'capacidade', 'logradouro', 'numero', 'bairro',
            'cidade', 'estado', 'complemento', 'cep', 'locador'
        )


class TipoRecursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = TipoRecurso
        fields = (
            'id', 'nome', 'figura_url'
        )


class RecursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recurso
        fields = (
            'id', 'quantidade', 'preco', 'sala', 'tipo_recurso'
        )


class GaleriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Galeria
        fields = (
            'id', 'descricao', 'url', 'principal', 'sala'
        )
