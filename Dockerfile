FROM python:3.11

WORKDIR /app
COPY ./requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
RUN apt-get update -qq && apt-get -y install mariadb-server
# SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode,'ONLY_FULL_GROUP_BY',''));
# source db_script/script.sql
# docker run --env-file env.list ubuntu env | grep VAR
ENTRYPOINT ["flask", "run"]