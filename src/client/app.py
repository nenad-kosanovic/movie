import os

# App Initialization
from . import create_app  # from __init__ file

app = create_app(os.getenv("CONFIG_MODE"))

# ----------------------------------------------- #


# Hello World!
@app.route("/")
def hello():
    return "Hello World!"

from .movies import urls

# ----------------------------------------------- #

if __name__ == "__client__":
   app.run(host="localhost", port=5001, debug=True)
