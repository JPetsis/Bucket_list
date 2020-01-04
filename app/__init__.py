import os
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from instance.config import app_config

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

db = SQLAlchemy()


def create_app(config_name):
  app = FlaskAPI(__name__, instance_relative_config = True)
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)
  return app
  

