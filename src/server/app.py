import os

from . import create_app

app = create_app(os.getenv("CONFIG_MODE"))


@app.route("/")
def hello():
    return "Hello World!"


from .movies import urls

if __name__ == "__server__":
    app.run(host="localhost", port=5000, debug=True)
