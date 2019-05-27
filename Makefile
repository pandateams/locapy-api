clean:
	 sudo find . -name '*.pyc' -delete && sudo find . -name '__pycache__' -delete

docker-clean:
	sudo docker system prune -af --volumes

container-createsuperuser:
	sudo docker exec -it locapy_api bash -c "python manage.py createsuperuser"

test:
    python manage.py test