# -*- coding: utf-8 -*-
from Models.Response import Response
from flask import Blueprint
import requests
import json

BLUEPRINT = Blueprint(__name__, '', url_prefix='/Hever')


class Hever(object):
    HEVER_LOGIN_URL = 'HTTPS://hvr.co.il/signin.aspx'
    HEVER_HOME_PAGE = r'https://www.hvr.co.il/home_page.aspx?page=hvr_home'

    def __init__(self):
        raise NotImplementedError('')

    @staticmethod
    @BLUEPRINT.route('/GetHeverInfo', methods=['POST'])
    def get_hever_info():
        return Response.succeed_response(None)

    @staticmethod
    def write_file(text):
        with open('C:\\Users\\Bar\\AppData\\Local\\Temp\\temp.html', 'wb') as file_handle:
            file_handle.write(text)

    @staticmethod
    def is_logged_in(content):
        x = u'שגויים'
        return x not in content.decode('cp1255')

    @staticmethod
    def parse_cookies_to_string(cookies):
        sum = ''

        for key in cookies.keys():
            sum += key + '=' + cookies[key] + '&'

        sum = sum[:-1]
        return sum

    @staticmethod
    def login(user_name, password, session, cookies):
        data = {'tz': user_name, 'password': password, 'oMode': 'login', 'reffer': ''}

        headers = {
            'Referer': 'https://www.hvr.co.il/signin.aspx',
            'Host': 'www.hvr.co.il',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Origin': 'https://www.hvr.co.il',
            'Upgrade-Insecure-Requests': '1',
            'Connection': 'keep-alive',
            'Cookie': Hever.parse_cookies_to_string(cookies)}

        response = session.post(Hever.HEVER_LOGIN_URL, data=data, headers=headers, verify=True)
        if Hever.is_logged_in(response.content):
            print 'Connected to hever'
            print response.cookies.get_dict()
            temp = session.cookies.get_dict()
            temp['bn'] = cookies['bn']
            headers['Cookies'] = Hever.parse_cookies_to_string(temp)
            headers['Referer'] = 'https://www.hvr.co.il/signin.aspx'
            print headers['Cookies']
            response = session.get(Hever.HEVER_HOME_PAGE, headers=headers)

            text = response.text
            Hever.write_file(text.encode('cp1255'))
        else:
            print 'Couldnt connect'

    @staticmethod
    def get_cookies(session):
        session.get(Hever.HEVER_LOGIN_URL)
        temp = session.cookies.get_dict()

        return temp

    @staticmethod
    def test():
        session = requests.Session()
        cookies = Hever.get_cookies(session)
        Hever.login('', '', session, cookies)
