FROM python:3.8
RUN mkdir /tmp/nata
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update
RUN apt-get install -y mosquitto mosquitto-clients
RUN pip3 install paho-mqtt
COPY . .
CMD [ "python", "./pub.py" ]
