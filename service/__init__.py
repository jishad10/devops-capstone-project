"""
Package: service
Initialize the Flask app and set up logging
"""
import sys
from flask import Flask
from flask_talisman import Talisman
from flask_cors import CORS
from service import config
from service.common import log_handlers

app = Flask(__name__)
app.config.from_object(config)

# Set up CORS policy
CORS(app)

# Set up Talisman for security headers
# force_https=False is important for the lab/CI environment (no HTTPS locally)
talisman = Talisman(app, force_https=False)

from service import routes, models  # noqa: F401
from service.common import error_handlers, cli_commands  # noqa: F401

try:
    models.init_db(app)
except Exception as error:
    app.logger.critical("%s: Cannot continue", error)
    sys.exit(4)

log_handlers.init_logging(app, "gunicorn.error")

app.logger.info(70 * "*")
app.logger.info("  A C C O U N T   S E R V I C E   R U N N I N G  ".center(70, "*"))
app.logger.info(70 * "*")

app.logger.info("Service initialized!")
