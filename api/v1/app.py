#!/usr/bin/python3
""" Web server endpoint """
from flask import Flask
from os import environ
from models import storage
from api.v1.views import app_views


app = Flask(__name__)
app.register_blueprint(app_views)

# Global strict slashes
app.url_map.strict_slashes = False


@app.teardown_appcontext
def tear_down(error=None):
    """ Close storage connection """
    storage.close()


if __name__ == "__main__":
    # Define host and port environment variables
    host = environ.get('HBNB_API_HOST', "0.0.0.0")
    port = environ.get('HBNB_API_PORT', 5000)

    app.run(host=host, port=port, threaded=True)
