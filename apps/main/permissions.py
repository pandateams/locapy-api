from rest_framework.permissions import BasePermission


class IsActive(BasePermission):
    """
    Allows access only to "is_active" users.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_active and request.user.perfil.bloqueado is False


class PlanoBronze(BasePermission):
    """
    Permite acesso apenas a quem tem o plano bronze
    """

    def has_permission(self, request, view):
        return request.user.perfil.perfil_locador.plano.nome == 'bronze'


class PlanoPrata(BasePermission):
    """
    Permite acesso apenas a quem tem o plano prata
    """

    def has_permission(self, request, view):
        return request.user.perfil.perfil_locador.plano.nome == 'prata'


class PlanoOuro(BasePermission):
    """
    Permite acesso apenas a quem tem o plano ouro
    """

    def has_permission(self, request, view):
        return request.user.perfil.perfil_locador.plano.nome == 'ouro'
