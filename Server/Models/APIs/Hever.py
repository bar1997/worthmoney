from Models.Response import Response
from flask import Blueprint

BLUEPRINT = Blueprint(__name__, '', url_prefix='/Hever')


class Hever (object):
    def __init__(self):
        raise NotImplementedError('')

    @staticmethod
    @BLUEPRINT.route('/GetHeverInfo', methods=['POST'])
    def get_hever_info():
        return Response.succeed_response(None)
