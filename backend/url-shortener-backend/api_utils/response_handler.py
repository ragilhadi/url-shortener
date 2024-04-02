from flask import jsonify
from .constants import APIStatus, APIReason, APIKey, URLKey


class ResponseHandler:
    def get_error_response(self, reason: str, error_code: int):
        response = {
            APIKey.READ: {},
            APIKey.STATUS: APIStatus.FAILED,
            APIKey.MESSAGE: reason,
        }
        return jsonify(response), error_code

    def get_success_response(self, data: dict):
        response = {
            APIKey.READ: data,
            APIKey.STATUS: APIStatus.SUCCESS,
            APIKey.MESSAGE: APIReason.SUCCESS_TASK,
        }
        return jsonify(response), 200

    def get_url_id_response(self, data: list):
        data = {
            URLKey.ID: data[0],
            URLKey.URL: data[1],
            URLKey.URL_SHORT: data[2],
            URLKey.VALID_UNTIL: data[3],
        }
        response = {
            APIKey.READ: data,
            APIKey.STATUS: APIStatus.SUCCESS,
            APIKey.MESSAGE: APIReason.SUCCESS_TASK,
        }
        return jsonify(response), 200
