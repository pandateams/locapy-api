# Serializers define the API representation.
from rest_framework import serializers

from apps.appexemplo.models import Example


class ExampleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Example
        fields = 'nome'
