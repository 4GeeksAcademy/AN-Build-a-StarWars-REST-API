from flask import Blueprint,jsonify, request
from models.user.user_model import User
from models.favorites.favorites_model import Favorites
from models import db

user_bp = Blueprint('user1',__name__)

@user_bp.route("/", methods=["GET"])
def list_users():
    users = User.query.all()
    return jsonify([user.serialize() for user in users]), 200

@user_bp.route("/users/favorites", methods=["GET"])
def list_user_favorites():
    """Lista todos los favoritos del usuario actual."""
    user_id = 1  # Simulación de un usuario actual
    favorites = Favorites.query.filter_by(user_id=user_id).all()
    return jsonify([favorite.serialize() for favorite in favorites]), 200

@user_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    """Devuelve la información de un usuario específico por su ID."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404
    return jsonify(user.serialize()), 200

@user_bp.route("/", methods=["POST"])
def create_user():
    """Crea un nuevo usuario"""
    data = request.get_json()
    if not data.get("email") or not data.get("password"):
        return jsonify({"error":"Se requiere el email y la contraseña"}), 400
    
    new_user = User(
        email=data.get("email"),
        password=data.get("password"),
        is_active=data.get("is_active", True)
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.serialize()),201

@user_bp.route("/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    """Actualiza la información de un usuario específico."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    data = request.get_json()
    user.email = data.get("email", user.email)
    user.is_active = data.get("is_active", user.is_active)

    db.session.commit()
    return jsonify(user.serialize()), 200


@user_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    """Elimina un usuario específico."""
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "Usuario no encontrado"}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "Usuario eliminado"}), 200