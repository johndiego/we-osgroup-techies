FROM django:3.0.7
MAINTAINER osgroup-techies.com

RUN mkdir -p /apt/demoproject

ADD cidemoapp/ /app/demoproject/

WORKDIR /app/demoproject/cidemoapp/

EXPOSE 8000

CMD ["python","manage.py","runserver 0:8000"]
