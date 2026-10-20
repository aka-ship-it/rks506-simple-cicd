"""Flask application serving a browser Snake game."""

from flask import Flask, send_from_directory

app = Flask(__name__, static_folder="static")


@app.route("/")
def index():
    """Serve the game page."""
    return send_from_directory(app.static_folder, "index.html")


@app.route("/health")
def health():
    """Health endpoint used by Docker and the pipeline."""
    return {"status": "ok"}
