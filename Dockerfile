FROM python:3
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD bash -c "sleep 10 &&
CMD python manage.py makemigrations
CMD python manage.py migrate
CMD echo \"from django.contrib.auth.models import User; User.objects.create_superuser('test', 'test@test.com', 'test')\" |
CMD python manage.py shell
CMD python manage.py runserver 0.0.0.0:8000"
