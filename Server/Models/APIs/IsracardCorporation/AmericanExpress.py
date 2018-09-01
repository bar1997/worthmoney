# -*- coding: utf-8 -*-
from Models.APIs.IsracardCorporation.IsracardGroup import IsracardGroup


class AmericanExpress(IsracardGroup):
    __AMERICAN_SEARCH_WORD = 'https://he.americanexpress.co.il/SearchResult/Search?query={0}&actionType=new&startPage={1}&inurl=all&siteName=amex'
    __FORBIDDEN_KEYWORDS = ['לא בתוקף']

    __CORPORATION_NAME = 'AmericanExpress'

    def __init__(self):
        super(AmericanExpress, self).__init__(corporation=AmericanExpress.__CORPORATION_NAME,
                                              search_url=AmericanExpress.__AMERICAN_SEARCH_WORD,
                                              forbidden_keywords=AmericanExpress.__FORBIDDEN_KEYWORDS)
