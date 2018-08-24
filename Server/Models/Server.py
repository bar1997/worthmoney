from Configurations.WebConfigurations import WebConfigurations
from flask import Flask, send_file

# Blueprints
from APIs.Hever import BLUEPRINT as HEVER_BLUEPRINT
from APIs.Example import BLUEPRINT as EXAMPLE_BLUEPRINT


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
    def get_main_page():
        return send_file('static/index.html')

    @staticmethod
    def initialize_routes():
        # GETS
        Server.__APP.add_url_rule('/', view_func=Server.get_main_page, methods=['GET'])

        # POSTS
        pass

    @staticmethod
    def initialize_blueprints():
        Server.__APP.register_blueprint(HEVER_BLUEPRINT)
        Server.__APP.register_blueprint(EXAMPLE_BLUEPRINT)

    @staticmethod
    def start(server_port):
        Server.initialize_routes()
        Server.initialize_blueprints()
        Server.__server_port = server_port
        Server.__APP.run(host='0.0.0.0', port=WebConfigurations.SERVER_PORT, threaded=True)
