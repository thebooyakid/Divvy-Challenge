from flask import Flask
from flask.signals import appcontext_tearing_down
from flask_migrate import Migrate
from config import Config
from divvy.models import db as root_db, ma
from .api.routes import api
from .site.routes import site

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api)
app.register_blueprint(site)

root_db.init_app(app)
migrate = Migrate(app, root_db)
ma.init_app(app)