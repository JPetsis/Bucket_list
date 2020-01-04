import os
from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from flask import request, jsonify, abort
from instance.config import app_config

APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
dotenv_path = os.path.join(APP_ROOT, '.env')
load_dotenv(dotenv_path)

db = SQLAlchemy()


def create_app(config_name):
  from app.models import Bucketlist

  app = FlaskAPI(__name__, instance_relative_config = True)
  app.config.from_object(app_config[config_name])
  app.config.from_pyfile('config.py')
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  db.init_app(app)
  
  @app.route('/bucketlists/', methods=['POST', 'GET'])
  def bucketlists():
    if request.method == "POST":
      name = str(request.data.get('name', ''))
      if name:
        bucketlist = Bucketlist(name = name)
        bucketlist.save()
        response = jsonify({
            'id': bucketlist.id,
            'name': bucketlist.name,
            'date_created': bucketlist.date_created,
            'date_modified': bucketlist.date_modified
        })
        response.status_code = 201
        return response
    else:
      # GET
      bucketlists = Bucketlist.get_all()
      results = []

      for bucketlist in bucketlists:
        obj = {
          'id': bucketlist.id,
          'name': bucketlist.name,
          'date_created': bucketlist.date_created,
          'date_modified': bucketlist.date_modified
        }
        results.append(obj)
      response = jsonify(results)
      response.status_code = 200
      return response
  
  
  
  return app
  

