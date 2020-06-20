from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class UserDealer(Resource):
    def __init__(self):
        self.url = 'url'

    def post(self):
        user_info = request.get_json()

api.add_resource(UserDealer, '/')