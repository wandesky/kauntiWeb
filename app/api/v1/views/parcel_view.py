from flask import Flask, Blueprint, jsonify, request
from app.api.v1.models.parcel_model import Parcel

parcels = Blueprint('parcels', __name__)

@parcels.route('/', methods=['GET'])
def get_parcels():
    return jsonify(Parcel.get_all_parcels())

@parcels.route('/<int:parcel_id>', methods=['GET'])
def get_parcel(parcel_id):
    # parcel = Parcel()
    return jsonify(Parcel.get_specific_parcel(None, parcel_id))

@parcels.route('/', methods=['POST'])
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

    parcel = Parcel(placedBy, weight, weightmetric, sentOn, deliveredOn, status, parcel_from, parcel_to, currentlocation)

    response = parcel.post_parcel()
    return response, 201