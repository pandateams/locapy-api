from django.contrib.auth.models import User

from apps.main.models import SoftDeletionModel


class Usuario(User, SoftDeletionModel):
    pass
