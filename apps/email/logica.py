from django.core.mail import send_mail
from django.template.loader import render_to_string


def envia_email_bemvindo(data):
    context = {
        'destinatario': [data['perfil']['usuario']['email']],
        'nome': data['nome_fantasia']
    }
    plain_text = f"Olá!! Parabens você está cadastrado no nosso melhor portal de aluguel de salas comerciais do Brasil"
    html_email = render_to_string('email/bem-vindo.html', context=context)
    assunto = 'Seja Bem vindo'
    remetente = 'controlapet@gmail.com'
    mail = send_mail(assunto, plain_text, remetente, context['destinatario'], html_message=html_email,
                     fail_silently=False)
    return mail
