from flask import Blueprint, request, jsonify
from app.controllers import human_controller

human_bp = Blueprint("human_bp", __name__)

@human_bp.route("/")
def welcome():
    return "Welcome to my homepage"

@human_bp.route("/add", methods=["POST"])
def add():
    data = request.get_json()
    try:
        message = human_controller.add_human(data)
        return jsonify({"message": message}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@human_bp.route("/get/<int:human_id>", methods=["GET"])
def get(human_id):
    row = human_controller.get_human(human_id)
    if row:
        return jsonify({
            "id": row[0],
            "name": row[1],
            "age": row[2],
            "job": row[3]
        })
    return jsonify({"message": "Human not found"}), 404

@human_bp.route("/all", methods=["GET"])
def list_all():
    humans = human_controller.list_humans()
    return jsonify([
        {"id": row[0], "name": row[1], "age": row[2], "job": row[3]}
        for row in humans
    ])
