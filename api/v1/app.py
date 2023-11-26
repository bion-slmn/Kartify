'''this module defines a flask app and registers the blueprint'''

from flask import Flask
from api.v1.views import app_views
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views, url_prefix='/api/v1')


if __name__ == "__main__":
    app.run(debug=True, threaded=True)
