from flask import Flask, request

app = Flask(__name__)


@app.get("/")
def hello():
    """Return a friendly HTTP greeting."""
    who = request.args.get("who", default="Learners!")
    return f"Hello {who}!\n\nWelcome to Google's App Engine Lab\n"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)