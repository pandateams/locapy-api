from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.locatario.tasks import envia_email_boas_vindas_locatario_task
from apps.locatario.api.serializers import LocatarioSerializer, LocatarioSerializerSoft
from apps.locatario.models import Locatario


class LocatarioViewSet(ModelViewSet):
    """
    Viewset responsavel pelo Locatario
    """
    serializer_class = LocatarioSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """
        Lista os locatarios ativos

        Returns
        -------
        Locatarios ativos
        """
        return Locatario.objects.filter(ativo=True)

    def create(self, request, *args, **kwargs):
        """
        Função que é chamada quando um Locatario está para ser criado

        Returns
        -------
        Objeto criado ou um objeto vazio
        """
        serializer = LocatarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            envia_email_boas_vindas_locatario_task(data=serializer.data)
            return Response(serializer.data, status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LocatarioViewSetSoft(ModelViewSet):
    """
    Viewset responsavel pelo Locatario
    """
    serializer_class = LocatarioSerializerSoft
    permission_classes = (IsAuthenticated,)

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
