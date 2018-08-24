from Models.Response import Response
from flask import Blueprint

BLUEPRINT = Blueprint(__name__, '', url_prefix='/Example')


class Example (object):
    def __init__(self):
        raise NotImplementedError('')

    @staticmethod
    @BLUEPRINT.route('/GetExampleInfo', methods=['POST'])
    def get_example_info():
        return Response.succeed_response(None)
