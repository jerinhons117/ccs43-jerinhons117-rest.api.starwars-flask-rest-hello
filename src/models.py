from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    favCharacters = db.relationship('FavCharacters', backref='user')
    FavPlanets = db.relationship('FavPlanets', backref='user')


    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name" : self.name,
            "is_active": self.is_active
            # do not serialize the password, its a security breach
        }
    
class FavCharacters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #aqui va las relaciones 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    characters_id = db.Column(db.Integer, db.ForeignKey('characters.id'))

    def __repr__(self):
        return '<FavCharacters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id
        }
    
class FavPlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    Planets_id = db.Column(db.Integer, db.ForeignKey('planets.id'))


    def __repr__(self):
        return '<FavPlanets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id
        }
    
class Characters(db.Model):
    __tablename__ = 'characters'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), unique=True, nullable=False)
    birth_year = db.Column(db.String(50), unique=True, nullable=False)
    species = db.Column(db.String(50), unique=True, nullable=False)
    height = db.Column(db.String(50), unique=True, nullable=False)
    mass = db.Column(db.String(50), unique=True, nullable=False)
    gender = db.Column(db.String(50), unique=True, nullable=False)
    hair_color = db.Column(db.String(50), unique=True, nullable=False)
    skin_color = db.Column(db.String(50), unique=True, nullable=False)
    homeworld = db.Column(db.String(50), unique=True, nullable=False)

    favCharacters = db.relationship('FavCharacters', backref='characters')


    def __repr__(self):
        return '<Characters %r>' % self.full_name

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "birth_year": self.birth_year,
            "species": self.species,
            "height": self.height,
            "mass": self.mass,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "homeworld": self.homeworld
        }
    
    
class Planets(db.Model):
    __tablename__= 'planets'
     # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50), unique=True, nullable=False)
    populations = db.Column(db.String(50), unique=True, nullable=False)
    rotarion_period = db.Column(db.String(50), unique=True, nullable=False)
    orbital_period = db.Column(db.String(50), unique=True, nullable=False)
    diameter = db.Column(db.String(50), unique=True, nullable=False)
    gravity = db.Column(db.String(50), unique=True, nullable=False)
    terrain = db.Column(db.String(50), unique=True, nullable=False)
    surface_water = db.Column(db.String(50), unique=True, nullable=False)
    climate = db.Column(db.String(50), unique=True, nullable=False)
    favPlanets = db.relationship('FavPlanets', backref='planets')

    def __repr__(self):
        return '<Planets %r>' % self.full_name

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "populations": self.populations,
            "rotarion_period": self.rotarion_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "gravity": self.gravity,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "climate": self.climate
        }
