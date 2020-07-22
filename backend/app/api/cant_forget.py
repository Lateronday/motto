from flask import Blueprint, jsonify
from flask_restful import Api, Resource


motto = Blueprint('motto', __name__)


api = Api(motto)


class List_Motto(Resource):

    @staticmethod
    def get():
        return jsonify(status=200, message='test')


api.add_resource(List_Motto, '/show')
