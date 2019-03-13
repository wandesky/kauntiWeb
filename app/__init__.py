from flask import Flask, Blueprint
from app.api.v1.views.parcel_view import parcels
from app.api.v1.views.user_view import users
from app.api.v1.views.edge_view import edges

app = Flask(__name__)
app.register_blueprint(parcels, url_prefix='/api/v1/parcels')
app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(edges, url_prefix='/')
