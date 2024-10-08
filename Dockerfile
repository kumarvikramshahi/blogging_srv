FROM python:3.9.6-slim-buster

WORKDIR /pkg

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--log-level", "critical"]
