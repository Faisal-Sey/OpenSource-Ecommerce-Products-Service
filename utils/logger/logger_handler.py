import logging


class CustomExternalHandler(logging.Handler):
    def __init__(self) -> None:
        super().__init__()

        # Initialize your external logging setup here, e.g.,
        # connect to a logging service

    def emit(self, record: logging.LogRecord) -> None:
        try:
            # Format the log record as needed
            log_entry = self.format(record)

            # Example: Send log_entry to an external logging service or system
            # Replace this with actual code to send logs to your external service
            print(f"Sending log to external service: {log_entry}")

        except Exception:
            self.handleError(record)

    def close(self) -> None:
        # Clean up or disconnect from the external logging service if necessary
        pass


# Configure logging
logger = logging.getLogger(
    __name__
)  # Logger for this module (__name__ resolves to current module)
logger.setLevel(
    logging.DEBUG
)  # Set the minimum logging level (e.g., DEBUG, INFO, ERROR)

# Define a handler for console output (you can add file handlers
# as shown in the previous example)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)  # Set the level for this handler

# Define a formatter
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
console_handler.setFormatter(formatter)

# Add the handler to the logger
logger.addHandler(console_handler)
