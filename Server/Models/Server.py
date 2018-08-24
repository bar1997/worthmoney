from Configurations.WebConfigurations import WebConfigurations
from flask import Flask, request, send_file


class Server (object):
    __APP = Flask(__name__)

    def __init__(self):
        raise NotImplementedError('')

    @staticmethod
    def get_main_page():
        return send_file('static/index.html')

    @staticmethod
    def initialize_routes():
        Server.__APP.add_url_rule('/', view_func=Server.get_main_page, methods=['GET'])

    @staticmethod
    def start(server_port):
        Server.initialize_routes()
        Server.__server_port = server_port
        Server.__APP.run(host='0.0.0.0', port=WebConfigurations.SERVER_PORT, threaded=True)
