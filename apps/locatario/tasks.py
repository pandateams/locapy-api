from celery.utils.log import get_task_logger

from apps.email.logica import envia_email
from locapy.celery import app

celery_logger = get_task_logger(__name__)


@app.task(bind=True, autoretry_for=(Exception,), retry_kwargs={'max_retries': 5})
def envia_email_boas_vindas_locatario_task(self, data):
    try:
        celery_logger.info(f"Enviando email de boas vindas ao locatario {data['nome']}")
        envia_email().boas_vindas_locatario(data=data)
    except Exception:
        celery_logger.info(f"Erro ao enviar email de boas vindas ao locatario {data['nome']}")
        self.retry(countdown=10 ** self.request.retries)
