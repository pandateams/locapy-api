from django.test import TestCase

from apps.autenticacao.models import Perfil, User
from apps.locador.models import Locador


class LocadorTeste(TestCase):
    """
    Teste para o model de Locador
    """

    def setUp(self):
        self.perfil = Perfil.objects.create(
            usuario=User.objects.create(username='user_teste', email='user_teste@gmail.com', password='Teste@123'))
        self.locador = Locador.objects.create(
            nome_fantasia='Industrias Stark', razao_social='Industrias Stark', inscricao_estadual=123456789123,
            cnpj='02511963000185', endereco='Manhatan',
            telefone='1629133122', perfil=self.perfil)

    def test_locador_str(self):
        self.assertEqual(self.locador.__str__(), 'Industrias Stark')

    def test_locador_repr(self):
        self.assertEqual(self.locador.__repr__(), 'Industrias Stark')
