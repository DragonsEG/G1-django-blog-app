FROM python:3.10.4

WORKDIR /blogapp

COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN apt-get update
EXPOSE 8000

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]