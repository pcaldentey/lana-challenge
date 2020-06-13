FROM tiangolo/uvicorn-gunicorn-fastapi:python3.6

COPY ./app /app
COPY ./client /client

RUN pip install --no-cache-dir -r /app/requirements.txt
