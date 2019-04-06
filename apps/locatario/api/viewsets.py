from rest_framework.viewsets import ModelViewSet

from apps.locatario.api.serializers import LocatarioSerializer, LocatarioSerializerSoft
from apps.locatario.models import Locatario


class LocatarioViewSet(ModelViewSet):
    """
    Viewset responsavel pelo Locatario
    """
    serializer_class = LocatarioSerializer
    permission_classes = ()

    def get_queryset(self):
        """
        Lista os locatarios ativos

        Returns
        -------
        Locatarios ativos
        """
        return Locatario.objects.filter(ativo=True)


class LocatarioViewSetSoft(ModelViewSet):
    """
    Viewset responsavel pelo Locatario
    """
    serializer_class = LocatarioSerializerSoft
    permission_classes = ()

    def get_queryset(self):
        """
        Lista os locatarios ativos

        Returns
        -------
        Locatarios ativos
        """
        return Locatario.objects.filter(ativo=True)
