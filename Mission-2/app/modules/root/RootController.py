from flask import Blueprint, jsonify


root_blueprint = Blueprint('root', __name__)

@root_blueprint.route('', methods=['GET'])
def index():
    return jsonify({"message": "Hello, World!"})