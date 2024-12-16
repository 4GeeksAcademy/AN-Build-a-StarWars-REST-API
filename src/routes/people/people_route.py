from flask import Blueprint, jsonify


people_bp = Blueprint('people_bp', __name__)


# Listar todas las personas
@people_bp.route('/', methods=["GET"])
def get_all_people():
     return jsonify({"message": "Listado de todas las personas"}), 200

# Obtener información de una sola persona por ID
@people_bp.route('/<int:people_id>', methods=["GET"])
def get_single_person(people_id):
 return jsonify({"people_id": people_id}), 200