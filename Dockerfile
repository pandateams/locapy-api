FROM python:3.7.2-slim-stretch

# Variaveis de ambiente
ARG requirements="prod"
ENV PYTHONUNBUFFERED 1
ENV DOTENV_PATH /app/.env
ENV DJANGO_SETTINGS_MODULE=locapy.settings.prod

# Copia o codigo para /app
COPY . /app
WORKDIR /app

# Instala requisitos
RUN pip install -r conf/requirements/prod.txt
RUN touch .env

### Limpa cache .deb
RUN apt clean
RUN apt autoclean

# Limpa o cache ou qualquer lixo que venha instalado
RUN find /app -name '*.pyc' -delete
RUN find /app -name '__pycache__' -delete
RUN rm -fr .idea .git* .python-version package-lock.json .pytest_cache

# Run the app.  CMD is required to run on Heroku
# $PORT is set by Heroku
CMD python manage.py runserver 0.0.0.0:$PORT
