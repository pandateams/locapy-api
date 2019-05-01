from decouple import config
from django.core.mail import send_mail
from django.template.loader import render_to_string


class EnviaEmail:
    def __init__(self):
        self.remetente = config('EMAIL_USER')

    def boas_vindas_locador(self, data):
        assunto = f"Bem vindo ao Locapy, {data['nome_fantasia']}!"
        destinatario = [data['perfil']['usuario']['email'], ]
        plain_text = f"Olá!! Parabens você está cadastrado no nosso melhor portal de aluguel de salas comerciais do Brasil"
        html_email = render_to_string('email/bem-vindo-locador.html', context=data)
        mail = send_mail(assunto, plain_text, self.remetente, destinatario, html_message=html_email,
                         fail_silently=False)
        return mail

    def boas_vindas_locatario(self, data):
        assunto = f"Bem vindo ao Locapy, {data['nome']}!"
        destinatario = [data['perfil']['usuario']['email'], ]
        plain_text = f"Olá!! Parabens você está cadastrado no nosso melhor portal de aluguel de salas comerciais do Brasil"
        html_email = render_to_string('email/bem-vindo-locatario.html', context=data)
        mail = send_mail(assunto, plain_text, self.remetente, destinatario, html_message=html_email,
                         fail_silently=False)
        return mail

    # def sala_cadastrada(self, data):
    #     destinatario = [data['perfil']['usuario']['email'], ]
    #     plain_text = f"Olá!! Parabens você está cadastrado no nosso melhor portal de aluguel de salas comerciais do Brasil"
    #     html_email = render_to_string('email/bem-vindo-locatario.html', context=data)
    #     assunto = 'Bem vindo ao Locapy!'
    #     mail = send_mail(assunto, plain_text, self.remetente, destinatario, html_message=html_email,
    #                      fail_silently=False)
    #     return mail


envia_email = EnviaEmail
