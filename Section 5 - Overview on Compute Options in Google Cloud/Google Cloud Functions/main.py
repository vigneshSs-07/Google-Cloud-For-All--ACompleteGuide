import flask


def hello_world(request: flask.Request) -> flask.Response:
    """HTTP Cloud Function.

    Returns:
    - "Hello Message! "
    """
    response = "Hello Learners! Cloud Function is Triggered and returned 200 message"

    return flask.Response(response, mimetype="text/plain")

