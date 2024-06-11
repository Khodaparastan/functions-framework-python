import logging
import time

logger = logging.getLogger(__name__)


def print_message(request):
    json = request.get_json(silent=True)
    print(json.get("message"))
    return "success", 200


def log_message(request):
    json = request.get_json(silent=True)
    logger.warning(json.get("message"))
    return "success", 200


def function(request):
    return {"execution_id": request.headers.get("Function-Execution-Id")}


def error(request):
    return 1 / 0


def sleep(request):
    json = request.get_json(silent=True)
    message = json.get("message")
    logger.warning(message)
    time.sleep(1)
    logger.warning(message)
    return "success", 200
