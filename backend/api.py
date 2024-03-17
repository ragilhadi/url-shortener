from app_initializer import app
from flask import request, jsonify, session
from flask_apscheduler import APScheduler
import time
import uuid
from typing import Tuple
from logger import get_logger, LogType
from api_utils.response_handler import ResponseHandler
from constants import ServiceStatus, DOCKER_TAG
import json
from datetime import datetime
import sqlite3
from database.action import URLAction

logger = get_logger()
scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()
logger(
    request_method="",
    response="",
    message="API READY",
    stack_trace="",
    log_type=LogType.INFO,
)
response_handler: ResponseHandler = ResponseHandler()
url_action: URLAction = URLAction()


@scheduler.task("interval", id="do_job_1", seconds=5)
def job1():
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    print(datetime.now())
    for user in data:
        valid_until = user.get("valid_until")
        valid_until =  datetime.strptime(valid_until, '%d-%m-%y %H:%M:%S')
        if valid_until < datetime.now():
            data.remove(user)
            print(f"Removed {user.get('url')}")
        else:
            print(f"Valid {user.get('url')}")
    with open("data.json", "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


@app.route("/url", methods=["GET"], provide_automatic_options=False)
def get_url() -> Tuple[dict, int]:
    """
    Get URL endpoint.

    Returns:
        Tuple[dict, int]: A tuple containing the response and HTTP status code.
    """
    try:
        result, count = url_action.get_count_url()
        if result:
            return response_handler.get_success_response({"database_count": count})
        else:
            return response_handler.get_error_response(reason="Internal server error", error_code=500)
    except FileNotFoundError:
        return response_handler.get_error_response(reason="File not found", error_code=404)


@app.route("/url/<id_url>", methods=["GET"], provide_automatic_options=False)
def get_url_id(id_url) -> Tuple[dict, int]:
    """
    Get URL by ID endpoint.

    Returns:
        Tuple[dict, int]: A tuple containing the response and HTTP status code.
    """
    try:
        result, data = url_action.get_url_by_id(id_url)
        if result:
            if data is None:
                return response_handler.get_error_response(reason="URL not found", error_code=404)
            return response_handler.get_url_id_response(data)
        else:
            return response_handler.get_error_response(reason="Internal server error", error_code=500)
    except Exception as e:
        return response_handler.get_error_response(reason=e, error_code=404)


@app.route("/url", methods=["POST"], provide_automatic_options=False)
def add_url() -> Tuple[dict, int]:
    """
    Add URL endpoint.

    Returns:
        Tuple[dict, int]: A tuple containing the response and HTTP status code.
    """
    try:
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            user = request.json
            url_action.add_url(user.get("url"), user.get("url_short"), user.get("valid_until"))
            return response_handler.get_success_response("")
        else:
            return response_handler.get_error_response(reason="Invalid content type", error_code=400)
    except FileNotFoundError:
        return response_handler.get_error_response(reason="File not found", error_code=404)


@app.route("/health", methods=["GET"], provide_automatic_options=False)
def healthcheck() -> Tuple[dict, int]:
    """
    Healthcheck endpoint.

    Returns:
        Tuple[dict, int]: A tuple containing the health status response and HTTP status code.
    """
    return (
        jsonify(
            {
                "version": DOCKER_TAG,
                "status": ServiceStatus.UP.value,
                "details": {},
            }
        ),
        200,
    )


@app.before_request
def before_request():
    """
    Before request hook.
    """
    # Store the start time for the request
    app.request_id = request.headers.get("x-request-id")
    if not app.request_id:
        app.request_id = str(uuid.uuid4())
    session["request_id"] = app.request_id
    app.start_time = time.time()

    logger(
        request_method=request.method,
        response="",
        message=f"Request Received to {request.path}",
        stack_trace="",
        log_type=LogType.INFO,
    )


@app.after_request
def after_request(response):
    """
    After request hook.

    Args:
        response (Response): The response object.

    Returns:
        Response: The modified response object.
    """
    total_time = time.time() - app.start_time
    time_in_seconds = round(total_time, 3)

    logger(
        request_method=request.method,
        response={
            "response": response,
            "status_code": response.status_code,
            "response_time": time_in_seconds,
        },
        message=f"Request Completed to {request.path} with time {time_in_seconds} seconds",
        stack_trace="",
        log_type=LogType.INFO,
    )

    return response
