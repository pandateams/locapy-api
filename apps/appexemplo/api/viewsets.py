# ViewSets define the view behavior.
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from apps.appexemplo.api.rest_serializer import ExampleSerializer
from apps.appexemplo.models import Example


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('nome',)
