from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.locador.api.serializers import LocadorSerializer, LocadorSerializerSoft
from apps.locador.models import Locador


class LocadorViewSet(ModelViewSet):
    """
    Viewset mais completa responsavel pelo locador
    """
    serializer_class = LocadorSerializer
    permission_classes = (AllowAny,)

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
    permission_classes = (AllowAny,)

    def get_queryset(self):
        """
        Função que filtra os locadores

        Returns
        -------
        Lista de locadores
        """

        return Locador.objects.filter(perfil__bloqueado=False)

    @action(methods=['get'], detail=False)
    def busca_cnpj(self, request):
        """
        Action que busca o cnpj para garantir a unicidade

        Parameters
        ----------
        request

        Returns
        -------
        Locador serializado ou um objeto vazio

        """
        try:
            query = Locador.objects.get(cnpj__exact=request.query_params['cnpj'])
            locador = LocadorSerializer(query)
            return Response(locador.data, status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({}, status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({}, status.HTTP_400_BAD_REQUEST)
