from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.autenticacao.api.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    """
    Viewset responsavel pelos usuários
    """
    serializer_class = UserSerializer
    permission_classes = ()

    def get_queryset(self):
        """
        Função que filtra os usuários

        Returns
        -------
        Lista de usuários
        """
        return User.objects.all()

    @action(methods=['get'], detail=False)
    def busca_username(self, request):
        try:
            query = User.objects.get(username__iexact=request.query_params['username'])
            user = UserSerializer(query)
            return Response(user.data, status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({}, status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({}, status.HTTP_400_BAD_REQUEST)

    @action(methods=['get'], detail=False)
    def busca_email(self, request):
        try:
            query = User.objects.get(email__exact=request.query_params['email'])
            user = UserSerializer(query)
            return Response(user.data, status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({}, status.HTTP_404_NOT_FOUND)
        except Exception:
            return Response({}, status.HTTP_400_BAD_REQUEST)
