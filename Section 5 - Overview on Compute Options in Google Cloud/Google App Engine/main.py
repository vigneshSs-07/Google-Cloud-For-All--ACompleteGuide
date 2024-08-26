import flask

app = flask.Flask(__name__)


@app.get("/")
def hello():
    """Return a friendly HTTP greeting."""
    return "\nHello Learners!\n\nWelcome to Google's App Engine Lab\n"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
    