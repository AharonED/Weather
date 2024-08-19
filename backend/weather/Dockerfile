FROM python:3.12
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app_be
WORKDIR /app_be
COPY ./requirements.txt /app_be/requirements.txt
RUN pip install -r requirements.txt
COPY . /app_be
CMD pip install -r requirements.txt

# CMD python manage.py runserver 0.0.0.0:8000
# CMD python -m debugpy --listen 0.0.0.0:5678 manage.py runserver 0.0.0.0:8000
