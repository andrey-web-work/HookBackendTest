FROM python:3.12

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

COPY backend /backend
COPY configs /configs

WORKDIR /backend

RUN pip install -r requirements-docker.txt --no-cache-dir

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
