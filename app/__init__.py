from flask import Flask, Blueprint
from app.api.v1.views.permit_view import permits
# from app.api.v1.views.user_view import users
from app.api.v1.views.edge_view import edges

app = Flask(__name__)
app.register_blueprint(permits, url_prefix='/api/v1/permits')
# app.register_blueprint(users, url_prefix='/api/v1/users')
app.register_blueprint(edges, url_prefix='/')
