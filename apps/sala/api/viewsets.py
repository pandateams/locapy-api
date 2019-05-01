from raven.contrib.django.models import client
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.sala.api.serializers import SalaSerializer, RecursoSerializer, TipoRecursoSerializer, GaleriaSerializer
from apps.sala.models import Sala, Recurso, TipoRecurso, Galeria


class SalaViewset(ModelViewSet):
    """
    Viewset responsavel pelas Salas
    """
    serializer_class = SalaSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        """
        Lista as salas

        Returns
        -------
        Salas
        """
        return Sala.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Função que é chamada quando uma Sala está para ser criada

        Returns
        -------
        Objeto criado ou um objeto vazio
        """
        serializer = SalaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            client.captureException()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RecursoViewset(ModelViewSet):
    """
    Viewset responsavel pelos recursos da sala
    """
    serializer_class = RecursoSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        """
        Lista os recursos da sala

        Returns
        -------
        Recursos
        """
        return Recurso.objects.all()


class TipoRecursoViewset(ModelViewSet):
    """
    Viewset responsavel pelo tipo de recurso das salas
    """
    serializer_class = TipoRecursoSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        """
        Lista os tipos de recursos da sala

        Returns
        -------
        Tipos de recursos
        """
        return TipoRecurso.objects.all()


class GaleriaViewset(ModelViewSet):
    """
    Viewset responsavel pelas fotos da sala
    """
    serializer_class = GaleriaSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        """
        Lista as fotos da sala

        Returns
        -------
        Objeto com urls das fotos
        """
        return Galeria.objects.all()
