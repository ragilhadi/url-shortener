import logging
import os
from flask import Flask
from logger import instantiate_logger
from utils import check_if_db_available
from database.init import initialize_schema

logging.captureWarnings(True)


class Config:
    SCHEDULER_API_ENABLED = True


if not check_if_db_available():
    initialize_schema()

app: Flask = Flask("api")
service_name = os.getenv("SERVICE_NAME", "flask-api")
app.request_id = None
app.secret_key = os.getenv("SESSION_SECRET_KEY", "secret-key")
app.logger = logging.getLogger("gunicorn.error")
app.config.from_object(Config())
instantiate_logger(app=app, service_name=service_name)
