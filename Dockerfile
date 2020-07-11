FROM python:3.7-slim
MAINTAINER osgroup-techies.com
RUN mkdir -p /opt/demoproject
ADD reqs.txt/ /opt/demoproject/
WORKDIR /opt/demoproject
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential \
libpq-dev \
libpcre3-dev 

RUN pip install -r reqs.txt

ADD cidemoapp/ /opt/demoproject
WORKDIR /opt/demoproject/cidemoapp
EXPOSE 8000

CMD ["python","manage.py","runserver 0:8000"]
