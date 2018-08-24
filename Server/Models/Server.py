import json
from Configurations.WebConfigurations import WebConfigurations
from flask import Flask, request, send_file


class Server (object):
    __APP = Flask(__name__)

    def __init__(self):
        raise NotImplementedError('')

    @staticmethod
    @__APP.after_request
    def after_request(response):
        header = response.headers
        header['Access-Control-Allow-Origin'] = '*'
        header['Access-Control-Allow-Headers'] = '*'
        return response

    @staticmethod
    def failed_response(message):
        return json.dumps({'Succeed': False, 'Message': message})

    @staticmethod
    def succeed_response(data):
        return json.dumps({'Succeed': True, 'Data': data})

    @staticmethod
    def get_main_page():
        return send_file('static/index.html')

    @staticmethod
    def example():
        return Server.succeed_response(None)

    @staticmethod
    def initialize_routes():
        Server.__APP.add_url_rule('/', view_func=Server.get_main_page, methods=['GET'])
        Server.__APP.add_url_rule('/Example', view_func=Server.example, methods=['POST'])

    @staticmethod
    def start(server_port):
        Server.initialize_routes()
        Server.__server_port = server_port
        Server.__APP.run(host='0.0.0.0', port=WebConfigurations.SERVER_PORT, threaded=True)
