from flask import Blueprint, jsonify,request
from models import db
from models.favorites.favorites_model import Favorites
from models.user.user_model import User
from datetime import date

favorites_bp = Blueprint('favorites_bp', __name__)


#
@favorites_bp.route("/favorite/planet/<int:planet_id>", methods=["POST"])
def add_favorite_planet(planet_id):
    """Agrega un nuevo planeta favorito."""
    user_id = 1  # Simulado
    new_fav = Favorites(
        user_id=user_id,
        planet_id=planet_id,
        favorite_type='planet',
        date_added=date.today()
    )
    db.session.add(new_fav)
    db.session.commit()
    return jsonify(new_fav.serialize()), 201


# Eliminar un planeta favorito
@favorites_bp.route("/favorite/planet/<int:planet_id>", methods=["DELETE"])
def delete_favorite_planet(planet_id):
    """Elimina un planeta favorito."""
    user_id = 1  # Simulado
    fav = Favorites.query.filter_by(user_id=user_id, planet_id=planet_id, favorite_type='planet').first()
    if not fav:
        return jsonify({"error": "Favorito no encontrado"}), 404
    db.session.delete(fav)
    db.session.commit()
    return jsonify({"message": "Favorito eliminado"}), 200


# Agregar una nueva persona como favorita para el usuario actual
@favorites_bp.route("/favorite/people/<int:people_id>", methods=["POST"])
def add_favorite_people(people_id):
    """Agrega una nueva persona como favorita."""
    user_id = 1  # Simulado
    new_fav = Favorites(
        user_id=user_id,
        planet_id=people_id,
        favorite_type='character',
        date_added=date.today()
    )
    db.session.add(new_fav)
    db.session.commit()
    return jsonify(new_fav.serialize()), 201


# Eliminar una persona favorita
@favorites_bp.route("/favorite/people/<int:people_id>", methods=["DELETE"])
def delete_favorite_people(people_id):
    """Elimina una persona como favorita."""
    user_id = 1  # Simulado
    fav = Favorites.query.filter_by(user_id=user_id, planet_id=people_id, favorite_type='character').first()
    if not fav:
        return jsonify({"error": "Favorito no encontrado"}), 404
    db.session.delete(fav)
    db.session.commit()
    return jsonify({"message": "Favorito eliminado"}), 200
