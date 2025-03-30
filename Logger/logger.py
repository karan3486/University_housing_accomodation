import logging
from flask import current_app

def get_logger():
    if current_app:
        return current_app.logger
    else:
        # If current_app is not available (e.g., outside a request context), use app.logger directly
        return logging.getLogger(__name__)  # or any other appropriate logger
