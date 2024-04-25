from flask import jsonify
from flask_restful import Api
from dotenv import load_dotenv, find_dotenv
import os

from app import app
from database import db

# Import Controllers
from sample.controller import *

#Import Models
from sample.model import Sample


api = Api(app)

prefix = "/api"

# Routes
api.add_resource(SampleController, f'{prefix}/sample/<int:sample_id>')
api.add_resource(SampleListController, f'{prefix}/sample')


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=os.getenv('PORT', 5000), debug=True)