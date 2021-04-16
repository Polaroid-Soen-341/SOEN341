FROM python

COPY ./requirements.txt /tmp/

RUN mkdir /app
WORKDIR /app

RUN python3 -m pip install -r /tmp/requirements.txt