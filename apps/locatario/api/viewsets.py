from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.locatario.api.serializers import LocatarioSerializer, LocatarioSerializerSoft
from apps.locatario.models import Locatario


class LocatarioViewSet(ModelViewSet):
    """
    Viewset responsavel pelo Locatario
    """
    serializer_class = LocatarioSerializer
    permission_classes = (AllowAny,)

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
    permission_classes = (AllowAny,)

    def get_queryset(self):
        """
        Lista os locatarios ativos

        Returns
        -------
        Locatarios ativos
        """
        return Locatario.objects.filter(ativo=True)

    @action(methods=['get'], detail=False)
    def busca_cpf(self, request):
        """
        Action que busca o cpf para garantir a unicidade

        Parameters
        ----------
        request

        Returns
        -------
        Locatario serializado ou um objeto vazio

        """
        try:
            query = Locatario.objects.get(cpf__exact=request.query_params['cpf'])
            locatario = LocatarioSerializer(query)
            return Response(locatario.data, status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({}, status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({}, status.HTTP_400_BAD_REQUEST)
