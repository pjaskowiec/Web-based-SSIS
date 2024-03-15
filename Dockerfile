FROM python:3.11

ARG username
ARG password
ARG host
ARG dbname

ENV username=$username
ENV password=$password
ENV host=$host
ENV dbname=$dbname

WORKDIR /app
COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt
COPY . .

EXPOSE 8080

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]
