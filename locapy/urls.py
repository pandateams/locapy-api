"""locapy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from apps.autenticacao.api.viewsets import UserViewSet, PerfilViewSetSoft, PerfilViewSet
from apps.locador.api.viewsets import LocadorViewSet, LocadorViewSetSoft
from apps.locatario.api.viewsets import LocatarioViewSet, LocatarioViewSetSoft
from apps.sala.api.viewsets import SalaViewset, TipoRecursoViewset, GaleriaViewset, RecursoViewset

router = routers.DefaultRouter()
router.register('usuario', UserViewSet, base_name='Usuario')
router.register('perfil', PerfilViewSetSoft, base_name='Perfil')
router.register('perfil-usuario', PerfilViewSet, base_name='Perfil Usuario')

router.register('cadastro/locador', LocadorViewSet, base_name='Cadastro Locador')
router.register('cadastro/locatario', LocatarioViewSet, base_name='Cadastro Locatario')
router.register('locador', LocadorViewSetSoft, base_name='Locador')
router.register('locatario', LocatarioViewSetSoft, base_name='Locatario')

router.register('sala', SalaViewset, base_name='Sala')
router.register('tipo-recurso', TipoRecursoViewset, base_name='Tipo Recurso')
router.register('recurso', RecursoViewset, base_name='Recurso')
router.register('galeria', GaleriaViewset, base_name='Galeria')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('auth/token/', obtain_auth_token)
]
