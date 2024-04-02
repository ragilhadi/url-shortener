class APIStatus:
    FAILED = "failed"
    SUCCESS = "success"


class APIReason:
    BAD_REQUEST = "bad request"
    INTERNAL_SERVER_ERROR = "internal server error"
    NOT_FOUND = "not found"
    FAILURE_TASK = "task failed"
    PENDING_TASK = "task is pending"
    STARTED_TASK = "task is in progress"
    SUCCESS_TASK = "task completed successfully"


class APIKey:
    STATUS = "status"
    MESSAGE = "message"
    READ = "read"

class URLKey:
    ID = "id"
    URL = "url"
    URL_SHORT = "url_short"
    VALID_UNTIL = "valid_until"
