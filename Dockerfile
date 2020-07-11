FROM python:3.7-slim
MAINTAINER osgroup-techies.com
RUN mkdir -p /apt/demoproject
ADD reqs.txt/ /app/demoproject/
WORKDIR /app/demoproject/
RUN apt-get update && apt-get install -y --no-install-recommends \
build-essential \
libpq-dev \
libpcre3-dev \

RUN pip install --no-cache-dir -r reqs.txt


EXPOSE 8000

CMD ["python","manage.py","runserver 0:8000"]
