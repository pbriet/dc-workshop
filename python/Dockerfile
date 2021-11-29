FROM python:3.9
ENV PYTHONUNBUFFERED 1

RUN pip install flask flask-mysqldb pytest

ENV PYTHONPATH /app
ENV FLASK_APP app
WORKDIR /app

COPY src/* /app/

EXPOSE 8080

CMD ["flask", "run", "--host=0.0.0.0", "--port=8080", "--without-threads"]