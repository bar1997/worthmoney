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
    def login(user_name, password, session, cookies):
        data = {'tz': user_name,
                'password': password,
                'oMode': 'login',
                'reffer': ''}

        headers = {'Referer': 'https://www.hvr.co.il/signin.aspx',
                   'Host': 'www.hvr.co.il',
                   'Content-Type': 'application/x-www-form-urlencoded',
                   'Origin': 'https://www.hvr.co.il',
                   'Upgrade-Insecure-Requests': '1',
                   'Connection': 'keep-alive',
                   'Cookie': cookies,
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

        print headers
        response = session.post(Hever.HEVER_LOGIN_URL, data=data, headers=headers, verify=True)
        print response.content
        print response.text
        print response.status_code
        '''
        if Hever.is_logged_in(response.content):
            print 'Connected to hever'
            headers = {'Cookie': 'zoom=1; ASP.NET_SessionId=fstf5zuychovulr2hl52xvu5; init_code=9142309255; tid=4230925; home_page=hvr_home; bn=; email=Bar.maor.1997@gmail.com; userfullname=%u05D1%u05E8%20%u05DE%u05D0%u05D5%u05E8; logout=signin.aspx' }
            response = session.get(Hever.HEVER_HOME_PAGE, headers=headers)
            text = response.text.encode('latin1').decode('cp1255')
            Hever.write_file(text.encode('cp1255'))
        else:
            print 'Couldnt connect'
        '''

    @staticmethod
    def get_cookies(session):
        session.get(Hever.HEVER_LOGIN_URL)
        return session.cookies.get_dict()

    @staticmethod
    def test():
        session = requests.Session()
        cookies = json.dumps(Hever.get_cookies(session)).lstrip('{').rstrip('}').replace('"', '')
        print cookies
        Hever.login('', '', session, cookies)
