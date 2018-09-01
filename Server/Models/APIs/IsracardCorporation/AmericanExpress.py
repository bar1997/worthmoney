# -*- coding: utf-8 -*-
from Models.APIs.IsracardCorporation.IsracardGroup import IsracardGroup
from Models.Response import Response
from flask import Blueprint

BLUEPRINT = Blueprint(__name__, '', url_prefix='/AmericanExpress')


class AmericanExpress(IsracardGroup):
    __AMERICAN_SEARCH_WORD = 'https://he.americanexpress.co.il/SearchResult/Search?query={0}&actionType=new&startPage={1}&inurl=all&siteName=amex'
    __FORBIDDEN_KEYWORDS = ['לא בתוקף']

    def __init__(self):
        super(AmericanExpress, self).__init__(search_url=AmericanExpress.__AMERICAN_SEARCH_WORD,
                                              forbidden_keywords=AmericanExpress.__FORBIDDEN_KEYWORDS)

    @staticmethod
    @BLUEPRINT.route('/GetAmericanInfo', methods=['POST'])
    def get_american_express_info():
        return Response.succeed_response(None)
