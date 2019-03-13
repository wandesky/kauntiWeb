from flask import Flask, Blueprint, jsonify, request
edges = Blueprint('edges', __name__)
error_message = {
                "message": "To get meaningful responses, try to channel your requests using the format ",
                "parcels": "https://send-it-adc-production.herokuapp.com/api/v1/parcels/ ",
                "users": "https://send-it-adc-production.herokuapp.com/api/v1/users/"
            }

@edges.route('', methods=['GET'])
@edges.route('/', methods=['GET'])
@edges.route('api/', methods=['GET'])
@edges.route('api/v1/', methods=['GET'])
def get_edges():
    return jsonify(
                error_message
            ), 200