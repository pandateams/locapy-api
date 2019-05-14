import json

from django.test import Client, TestCase
from rest_framework import status

from apps.autenticacao.models import Perfil, User
from apps.locador.api.serializers import LocadorSerializer, LocadorSerializerSoft
from apps.locador.models import Locador

# initialize the APIClient app
client = Client()


class PegaLocadoresCompletoTest(TestCase):
    """ Módulo de teste que pega os locadores"""

    def setUp(self):
        self.perfil = Perfil.objects.create(
            usuario=User.objects.create(username='user_teste', email='user_teste@gmail.com', password='Teste@123'))
        Locador.objects.create(
            nome_fantasia='Casper', cnpj=3, perfil=self.perfil)
        Locador.objects.create(
            nome_fantasia='Muffin', cnpj=1, perfil=self.perfil)
        Locador.objects.create(
            nome_fantasia='Rambo', cnpj=2, perfil=self.perfil)
        Locador.objects.create(
            nome_fantasia='Ricky', cnpj=6, perfil=self.perfil)

    def test_pega_todos_locadores_completos_validos(self):
        response = client.get('/cadastro/locador/')
        locadores = Locador.objects.all()
        serializer = LocadorSerializer(locadores, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pega_todos_locadores_validos(self):
        response = client.get('/locador/')
        locadores = Locador.objects.all()
        serializer = LocadorSerializerSoft(locadores, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pega_locador_completo_valido(self):
        locador = Locador.objects.get(nome_fantasia='Casper')
        response = client.get(f'/cadastro/locador/{locador.pk}/')
        serializer = LocadorSerializer(locador)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pega_locador_valido(self):
        locador = Locador.objects.get(nome_fantasia='Casper')
        response = client.get(f'/locador/{locador.pk}/')
        serializer = LocadorSerializerSoft(locador)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_pega_locador_completo_inexistente(self):
        response = client.get(f'/cadastro/locador/{564}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_pega_locador_inexistente(self):
        response = client.get(f'/locador/{564}/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CriaLocadoresCompletoTest(TestCase):
    """ Módulo de teste que cria locadores"""

    def setUp(self):
        self.valid_payloads = [
            {
                "nome_fantasia": "Tony Stark",
                "cnpj": "74701991000176",
                "perfil": {
                    "usuario": {
                        "username": "tony",
                        "email": "tony@gmail.com",
                        "password": "Teste123"
                    }
                }
            },
            {
                "nome_fantasia": "Steve Rogers",
                "cnpj": "74701991000177",
                "perfil": {
                    "usuario": {
                        "username": "steve",
                        "email": "steve@hotmail.com",
                        "password": "Teste123"
                    }
                }
            },
            {
                "nome_fantasia": "Bruce Banner",
                "cnpj": "74701991000178",
                "perfil": {
                    "usuario": {
                        "username": "bruce",
                        "email": "bruce@gmail.com",
                        "password": "Teste123"
                    }
                }
            }
        ]
        self.invalid_cnpj_payload = {
            "nome_fantasia": "Teste",
            "cnpj": "7491000176",
            "perfil": {
                "usuario": {
                    "username": "user_teste",
                    "email": "teste@gmail.com",
                    "password": "Teste123"
                }
            }
        }

    def test_cria_locador_valido(self):
        for payload in self.valid_payloads:
            response = client.post(
                '/cadastro/locador/',
                data=json.dumps(payload),
                content_type='application/json'
            )
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cria_locador_cnpj_invalido(self):
        response = client.post(
            '/cadastro/locador/',
            data=json.dumps(self.invalid_cnpj_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class AlteraLocadoresCompletoTest(TestCase):
    """ Módulo de teste que altera os locadores"""

    def setUp(self):
        self.perfil = Perfil.objects.create(
            usuario=User.objects.create(username='user_teste', email='user_teste@gmail.com', password='Teste@123'))
        self.locador = Locador.objects.create(
            nome_fantasia='Casper', cnpj=3, perfil=self.perfil)

        self.valid_payload = {
            "nome_fantasia": "Teste",
            "cnpj": "74701991000176",
            "perfil": 1
        }

    def test_altera_locador_completo(self):
        response = client.put(
            f'/cadastro/locador/{self.locador.pk}/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_altera_locador(self):
        response = client.put(
            f'/locador/{self.locador.pk}/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
