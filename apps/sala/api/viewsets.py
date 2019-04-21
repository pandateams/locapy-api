from rest_framework.permissions import AllowAny
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
