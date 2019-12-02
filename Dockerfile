FROM python:3.7

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV FLASK_ENV=docker

CMD ["python", "manage.py", "run"]

EXPOSE 5000
