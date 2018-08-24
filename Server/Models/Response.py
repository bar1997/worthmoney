import json


class Response (object):
    @staticmethod
    def failed_response(message):
        return json.dumps({'Succeed': False, 'Message': message})

    @staticmethod
    def succeed_response(data):
        return json.dumps({'Succeed': True, 'Data': data})
