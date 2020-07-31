FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY cidemoapp/reqs.txt /code/
RUN pip install -r reqs.txt
COPY . /code/
WORKDIR /code/cidemoapp/
EXPOSE 8000

CMD ["./app-manager.sh"]

