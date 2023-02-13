FROM python:3.9

RUN mkdir /talanakombat

WORKDIR /talanakombat

COPY . /talanakombat

CMD ["python3","./main.py"]