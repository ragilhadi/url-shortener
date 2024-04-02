FROM python:3.9.18-slim-bullseye AS builder

RUN apt-get update && \
    apt-get install -y git && \
    apt-get install -y libgl1-mesa-glx libglib2.0-0 && \
    pip install --upgrade pip setuptools

WORKDIR /app

COPY ./url-shortener-backend/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY ./url-shortener-backend .

HEALTHCHECK --interval=1m --timeout=1m --start-period=5s --retries=3 \
CMD curl --fail http://localhost:8810/health || exit 1

RUN chmod +x entrypoint.sh

EXPOSE 8810

ENTRYPOINT ["./entrypoint.sh"]