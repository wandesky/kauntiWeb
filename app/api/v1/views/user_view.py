from flask import Flask, Blueprint, jsonify, request
from app.api.v1.models.user_model import User
from app.api.v1.models.parcel_model import Parcel

users = Blueprint('users', __name__)

@users.route('/', methods=['GET'])
def get_users():
    return jsonify(User.get_all_users())

'''View function to retrieve all orders placed by specific user'''
@users.route('/<int:user_id>/parcels', methods=['GET'])
def get_orders_by_specific_user(user_id):
    orders = Parcel.get_orders_by_specific_user(None, user_id)
    return jsonify(orders), 200

@users.route('/', methods=['POST'])
def post_user():
    req_data = request.get_json()
    # user_id = req_data['id'] the id will be dynamically generated
    firstname = req_data['firstname']
    lastname = req_data['lastname']
    othernames = req_data["othernames"]
    email = req_data["email"]
    othernames = req_data["othernames"]
    email = req_data["email"]
    username = req_data["username"]
    registered = req_data["registered"]
    isAdmin = req_data["isAdmin"]

    user = User(firstname, lastname, othernames, email, username, registered, isAdmin)

    response = user.post_user()
    return response, 201