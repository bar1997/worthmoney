# -*- coding: utf-8 -*-
from Models.APIs.IsracardGroup import IsracardGroup
from Models.Response import Response
from flask import Blueprint

BLUEPRINT = Blueprint(__name__, '', url_prefix='/Isracard')


class Isracard(IsracardGroup):
    __ISRACARD_SEARCH_WORD = 'https://digital.isracard.co.il/SearchResult/Search?query={0}&actionType=new&startPage={1}&inurl=all&siteName=isracard'
    __FORBIDDEN_KEYWORDS = ['ההטבה הסתיימה']

    def __init__(self):
        super(Isracard, self).__init__(search_url=Isracard.__ISRACARD_SEARCH_WORD,
                                       forbidden_keywords=Isracard.__FORBIDDEN_KEYWORDS)

    @staticmethod
    @BLUEPRINT.route('/GetIsracardInfo', methods=['POST'])
    def get_isracard_info():
        return Response.succeed_response(None)
