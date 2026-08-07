from flask import Flask


def test_flask_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "NotesHub is working"

    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"NotesHub is working"
