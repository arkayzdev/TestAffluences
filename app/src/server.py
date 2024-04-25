from flask import jsonify
from flask_restful import Api
from dotenv import load_dotenv, find_dotenv
import os

from app import app
from database import db

# Import Controllers
from occupancy.controller import OccupancyListController



api = Api(app)

prefix = "/api"

# Routes
api.add_resource(OccupancyListController, f'{prefix}/occupancy')


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run(host="0.0.0.0", port=os.getenv('PORT', 5000), debug=True)