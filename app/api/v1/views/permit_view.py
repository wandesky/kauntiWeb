from flask import Flask, Blueprint, jsonify, request
from app.api.v1.models.permit_model import Permit

permits = Blueprint('permits', __name__)

@permits.route('/', methods=['GET'])
def get_parcels():
    return jsonify(Permit.get_all_parcels())

# Previous GET method for specific items
# @permits.route('/<int:parcel_id>', methods=['GET'])
# def get_parcel(parcel_id):
#     # parcel = Parcel()
#     return jsonify(Permit.get_specific_parcel(None, parcel_id))

@permits.route('/<string:parcel_id>', methods=['GET'])
def get_parcel(parcel_id):
    # parcel = Parcel()
    return jsonify(Permit.get_specific_parcel(None, parcel_id))

@permits.route('/', methods=['POST'])
def post_parcel():
    req_data = request.get_json()
    # parcel_id = req_data['id'] the id will be dynamically generated
    placedBy = req_data['placedBy']
    weight = req_data['weight']
    weightmetric = req_data["weightmetric"]
    sentOn = req_data["sentOn"]
    deliveredOn = req_data["deliveredOn"]
    status = req_data["status"]
    parcel_from = req_data["parcel_from"]
    parcel_to = req_data["parcel_to"]
    currentlocation = req_data["currentlocation"]

    permit = Permit(placedBy, weight, weightmetric, sentOn, deliveredOn, status, parcel_from, parcel_to, currentlocation)

    response = permit.post_parcel()
    return response, 201