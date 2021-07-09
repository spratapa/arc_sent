FROM python:3.7

COPY ./requirements.txt  /app1/requirements.txt

WORKDIR /app1

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

COPY . /app1

EXPOSE 5000

ENTRYPOINT ["python"]

CMD ["app1.py"] 