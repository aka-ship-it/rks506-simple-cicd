"""Simple Flask application for the RKS506 CI/CD project."""

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>CI/CD Demo</title>
    </head>
    <body>
        <h1>Hello from RKS506!</h1>
        <p>This is a learning project about CI/CD</p>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
