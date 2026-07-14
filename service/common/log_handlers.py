"""
Log Handlers
"""
import logging


def init_logging(app, logger_name="gunicorn.error"):
    """Set up logging for production"""
    logger = logging.getLogger(logger_name)
    if logger.handlers:
        app.logger.handlers = logger.handlers
        app.logger.setLevel(logger.level)
    app.logger.propagate = False

    for handler in app.logger.handlers:
        formatter = logging.Formatter(
            "[%(asctime)s] [%(levelname)s] [%(module)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        handler.setFormatter(formatter)

    app.logger.info("Logging handler established")
