FROM python:3.7-slim-stretch

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY status_client.py /usr/src/app
COPY status_pb2.py /usr/src/app
COPY status_pb2_grpc.py /usr/src/app
COPY app.py /usr/src/app

EXPOSE 5001/tcp
EXPOSE 5000/tcp

CMD ["python", "app.py"]
# CMD ["python", "status_client.py"]