"""Simple Flask application for the RKS506 CI/CD project."""

from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    """Return the CI/CD demo homepage."""
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Demo</title>
    </head>
    <body>
        <h1>Hello from RKS506!</h1>
        <p>This is a learning project about CI/CD</p>
        <p>Server time: {current_time}</p>
    </body>
    </html>
    """
