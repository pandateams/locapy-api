from rest_framework.viewsets import ModelViewSet

from apps.locador.api.serializers import LocadorSerializer, LocadorSerializerSoft
from apps.locador.models import Locador


class LocadorViewSet(ModelViewSet):
    """
    Viewset mais completa responsavel pelo locador
    """
    serializer_class = LocadorSerializer
    permission_classes = ()

    def get_queryset(self):
        """
        Função que filtra os locadores

        Returns
        -------
        Lista de locadores
        """

        return Locador.objects.filter(perfil__bloqueado=False)


class LocadorViewSetSoft(ModelViewSet):
    """
    Viewset mais simples responsavel pelo locador
    """
    serializer_class = LocadorSerializerSoft
    permission_classes = ()

    def get_queryset(self):
        """
        Função que filtra os locadores

        Returns
        -------
        Lista de locadores
        """

        return Locador.objects.filter(perfil__bloqueado=False)
