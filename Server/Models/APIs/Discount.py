# -*- coding: utf-8 -*-
import json
import unicodedata
import ast
import requests
from Models.Response import Response
from flask import Blueprint

BLUEPRINT = Blueprint(__name__, '', url_prefix='/Discount')


class Discount(object):
    DISCOUNT_SEARCH_WORD = 'https://www.icmega.co.il/org/search.aspx?v=1&searchWord={0}'

    def __init__(self):
        raise NotImplementedError('')

    @staticmethod
    @BLUEPRINT.route('/GetDiscountInfo', methods=['POST'])
    def get_discount_info():
        return Response.succeed_response(None)

    @staticmethod
    def normalize_text(text):
        normalized = unicodedata.normalize('NFKD', text)
        no_nikkud = ''.join([c for c in normalized if not unicodedata.combining(c)])
        return no_nikkud

    @staticmethod
    def __get_items_by_search_word(search_word):
        with requests.Session() as session:

            headers = {
                'Upgrade-Insecure-Requests': '1',
                'Host': 'www.icmega.co.il',
                'Upgrade-Insecure-Requests': '1',
                'Connection': 'keep-alive'
            }
            response = session.get(url=Discount.DISCOUNT_SEARCH_WORD.format(search_word), headers=headers)
            print response.content
            # data = json.loads(ast.literal_eval(response.content))

        return []

    @staticmethod
    def get_cookies():
        cookies_url = 'http://www.icmega.co.il/org/search.aspx?v=1&searchWord=%F1%E9%F0%EE%E4%20%F1%E9%E8%E9 HTTP/1.1'
        with requests.Session() as session:

            headers = {
                'Host': 'www.icmega.co.il',
                'Connection': 'keep-alive',
                'Pragma': 'no-cache',
                'Cache-Control': 'no-cache',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Referer': 'http://www.icmega.co.il/org/search.aspx?v=1&searchWord=%F1%E9%F0%EE%E4%20%F1%E9%E8%E9',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'he-IL,he;q=0.9,en-US;q=0.8,en;q=0.7',
                'Cookie': 'ASP.NET_SessionId=h45q0tqj5sarbqzbbe5uvjh3; org_id=20; logout=http://www.icmega.co.il/org/logout.aspx%3Fu%3Dhttp%3A//www.mafteach.co.il; logo=; userfullname=%u05DE%u05E4%u05EA%u05D7%20%u05D3%u05D9%u05E1%u05E7%u05D5%u05E0%u05D8; zoom=1; tblPage=%7B%22page%22%3A1%2C%22combo_id%22%3A-1%2C%22text%22%3A%22%22%7D'
            }
            response = session.get(url=Discount.DISCOUNT_SEARCH_WORD.format(cookies_url), headers=headers)
            print response.content

    @staticmethod
    def get_coupons_by_input():

        print Discount.get_cookies()
        # items = Discount.__get_items_by_search_word(user_input)
        # print items
