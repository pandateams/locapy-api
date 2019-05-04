from django.core.exceptions import ObjectDoesNotExist
from raven.contrib.django.raven_compat.models import client
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.email.logica import envia_email
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

    def create(self, request, *args, **kwargs):
        """
        Função que é chamada quando um Locador está para ser criado

        Returns
        -------
        Objeto criado ou um objeto vazio
        """
        serializer = LocadorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            envia_email().boas_vindas_locador(data=serializer.data)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            client.captureException()
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Função que é chamada quando um Locador é atualizado

        """
        return Response('', status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        Função que é chamada quando um Locador é deletado

        """
        return Response('', status=status.HTTP_400_BAD_REQUEST)


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
            client.captureException()
            return Response({}, status.HTTP_400_BAD_REQUEST)
