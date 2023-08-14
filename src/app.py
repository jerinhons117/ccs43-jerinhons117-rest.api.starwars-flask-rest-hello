"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User, Characters, Planets, FavCharacters, FavPlanets
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False

db_url = os.getenv("DATABASE_URL")
if db_url is not None:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_url.replace("postgres://", "postgresql://")
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/user', methods=['POST'])
def handle_hello():

    response_body = {
        "msg": "Hello, this is your GET /user response "
    }

    return jsonify(response_body), 200



#character endpoint
#metodo get me trae todo los registros de character
@app.route('/people', methods=['GET'])
def handle_characters():
    characters = Characters.query.all()
    arr_characters =list( map(lambda character: character.serialize(), characters))
    print(arr_characters)
    return jsonify(arr_characters), 200
#metodo get me trae uno de character
@app.route('/people/<int:people_id>', methods=['GET'])
def handle_characters_id(people_id):
    characters = Characters.query.get(people_id)
    print(characters)
    return jsonify(characters.serialize()), 200

#planets endpoint

@app.route('/planets', methods=['GET'])
def handle_planets():
    planets = Planets.query.all()
    arr_planets = list( map(lambda planet: planet.serialize(), planets))
    print(arr_planets)
    return jsonify(arr_planets), 200


#metodo get me trae uno de character

@app.route('/planets/<int:planets_id>', methods=['GET'])
def handle_planet_single_id(planets_id):
    planet = Planets.query.get(planets_id)
    print(planet)
    return jsonify(planet.serialize()), 200


# @app.route("/favorite/people/<int:people_id>", methods=["POST"])
# def get_fav_character(id):
#    body = request.json
#    FavCharacters = body.query.get("FavCharacter.id")
#    print(FavCharacters)
#    return ""


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
