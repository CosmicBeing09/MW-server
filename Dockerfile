FROM python:3.9-slim-buster

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install --trusted-host pypi.python.org -r requirements.txt


EXPOSE 8080

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]

