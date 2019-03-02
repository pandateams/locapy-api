# ViewSets define the view behavior.
from rest_framework import viewsets

from apps.appexemplo.api.rest_serializer import ExampleSerializer
from apps.appexemplo.models import Example


class ExampleViewSet(viewsets.ModelViewSet):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
