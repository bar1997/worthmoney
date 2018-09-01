# -*- coding: utf-8 -*-
from Models.APIs.IsracardCorporation.IsracardGroup import IsracardGroup


class Isracard(IsracardGroup):
    __ISRACARD_SEARCH_WORD = 'https://digital.isracard.co.il/SearchResult/Search?query={0}&actionType=new&startPage={1}&inurl=all&siteName=isracard'
    __FORBIDDEN_KEYWORDS = ['ההטבה הסתיימה']

    __CORPORATION_NAME = 'Isracard'

    def __init__(self):
        super(Isracard, self).__init__(corporation=Isracard.__CORPORATION_NAME,
                                       search_url=Isracard.__ISRACARD_SEARCH_WORD,
                                       forbidden_keywords=Isracard.__FORBIDDEN_KEYWORDS)
