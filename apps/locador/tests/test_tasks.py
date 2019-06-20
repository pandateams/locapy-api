from django.test import TestCase
from mock import patch

from apps.locador.tasks import envia_email_boas_vindas_locador_task


class TestTasks(TestCase):
    """ Módulo de teste para testar as tasks de Locador"""

    def setUp(self):
        self.data = {
            'id': 1, 'nome_fantasia': 'Tony Stark', 'razao_social': None, 'inscricao_estadual': None,
            'cnpj': '74701991000176', 'endereco': None, 'telefone': None,
            'perfil': {
                'id': 1,
                    'usuario': {
                        'id': 1,
                        'username': 'tony',
                        'email': 'tony@gmail.com',
                        'password': 'Teste+123'
                    }
                }
            }

    @patch('apps.locador.tasks.envia_email')
    def test_envia_email_locador(self, mocked_function):
        envia_email_boas_vindas_locador_task(data=self.data)

        assert mocked_function().boas_vindas_locador.called is True
