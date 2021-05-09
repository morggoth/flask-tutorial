FROM python:alpine3.13

ENV FLASK_APP=microblog.py

COPY microblog /app

RUN pip install -r /app/requirements.txt

EXPOSE 5000

WORKDIR /app

ENTRYPOINT [ "flask", "run", "--host=0.0.0.0" ]