FROM python:3.6

RUN mkdir /opt/injazati

WORKDIR /opt/injazati

ADD . /opt/injazati/

EXPOSE 8000

RUN pip install -r requirements.txt

CMD ["./docker-entrypoint.sh"]
