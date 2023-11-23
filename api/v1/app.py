'''this module defines a flask app and registers the blueprint'''

from flask import Flask
from api.v1.views import app_views


app = Flask(__name__)
app.url_map.strict_slashes = False
app.register_blueprint(app_views, url_prefix='/api/v1')


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
