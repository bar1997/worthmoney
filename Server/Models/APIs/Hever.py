from Models.Response import Response
from flask import Blueprint
import requests

BLUEPRINT = Blueprint(__name__, '', url_prefix='/Hever')


class Hever(object):
    HEVER_LOGIN_URL = 'HTTPS://hvr.co.il/signin.aspx'

    def __init__(self):
        raise NotImplementedError('')

    @staticmethod
    @BLUEPRINT.route('/GetHeverInfo', methods=['POST'])
    def get_hever_info():
        return Response.succeed_response(None)

    @staticmethod
    def write_file(text):
        with open('C:\\Users\\Bar\\AppData\\Local\\Temp\\temp.html', 'wb') as file_handle:
            file_handle.write(text.encode('cp1255'))

    @staticmethod
    def login(user_name, password):
        data = {'tz': user_name,
                'password': password,
                'oMode': 'login',
                'tmpl_filename': 'signin',
                'reffer': '',
                'redirect': 'https%3A%2F%2Fwww.hvr.co.il%2Fhome_page.aspx%3Fpage%3Dhvr_home',
                'cn': '17818875500',
                'emailRestore': ''}
        headers = {'Referer': 'https://www.hvr.co.il/signin.aspx',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Origin': 'HTTPS://www.hvr.co.il',
                   'Upgrade-Insecure-Requests': '1',
                   'Cookie': 'zoom = 1',
                   'ASP.NET_SessionId': 'fstf5zuychovulr2hl52xvu5',
                   'init_code': '9142309255',
                   'tid': '4230925',
                   'bn': '1781887550, 161007234711807636'
                   }
        with requests.Session() as session:
            text = session.post(Hever.HEVER_LOGIN_URL, data=data, headers=headers, verify=True).text
            Hever.write_file(text)

    @staticmethod
    def test():
        Hever.login('208418632', '28051997')
