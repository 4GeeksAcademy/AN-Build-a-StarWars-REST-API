from flask import Blueprint, jsonify, request
from models.planet.planet_model import Planet
from models import db

planet_bp = Blueprint('planet_bp', __name__)


# Listar todas las personas
@planet_bp.route('/', methods=["GET"])
def list_planets():
    planets = Planet.query.all()
    return jsonify([planet.serialize() for planet in planets]), 200

# crear un nuevo planeta
@planet_bp.route("/", methods=["POST"])
def create_planet():
   data = request.get_json()
   new_planet = Planet(
      name=data.get('name'),
      description=data.get('description')
   )
   db.session.add(new_planet)
   db.session.commit()
   return jsonify(new_planet.serialize()),201

@planet_bp.route('/<int:planet_id>', methods=["DELETE"])
def delete_planet(planet_id):
    """Elimina un planeta por ID."""
    planet = Planet.query.get(planet_id)
    if not planet:
        return jsonify({"error": "Planeta no encontrado"}), 404
    db.session.delete(planet)
    db.session.commit()
    return jsonify({"message": "Planeta eliminado"}), 200