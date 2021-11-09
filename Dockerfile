FROM python:latest
RUN mkdir /code
COPY requirements.txt /code
RUN pip install --upgrade pip
RUN pip install -r /code/requirements.txt
COPY . /code/
WORKDIR /code/myshop
CMD python manage.py migrate
CMD python manage.py runserver 0.0.0.0:8000