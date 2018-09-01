# -*- coding: utf-8 -*-

from Models.APIs.CouponSite import CouponSite
from abc import ABCMeta, abstractmethod
from Coupon import Coupon

import json
import unicodedata
import ast
import requests
from Models.Response import Response
from flask import Blueprint


class IsracardGroup(CouponSite):
    __metaclass__ = ABCMeta

    def __init__(self, search_url, forbidden_keywords):
        super(IsracardGroup, self).__init__(search_url)
        self.__forbidden_keywords = forbidden_keywords

    def get_coupons_by_word(self, word):
        """
        :param word: String to search in site
        :return: list of filters Coupons
        """
        items = self.__get_items_by_search_word(word)
        coupons = []

        for page_items in items:
            for item in page_items['Items']:
                description = IsracardGroup.__normalize_text(item['snippet']).encode('utf-8')
                title = IsracardGroup.__normalize_text(item['title']).encode('utf-8')
                link = IsracardGroup.__normalize_text(item['link']).encode('utf-8')

                for forbidden_keyword in self.__forbidden_keywords:
                    user_input_in_search_results = word in title or word in description

                    if page_items['UsedSpelling']:
                        suggested_in_search_results = page_items['Suggested'] in title or page_items[
                            'Suggested'] in description

                        if (forbidden_keyword not in title) and (
                                suggested_in_search_results or user_input_in_search_results):
                            coupons.append(Coupon(title, description, link))
                    else:
                        if (forbidden_keyword not in title) and user_input_in_search_results:
                            coupons.append(Coupon(title, description, link))
        return coupons

    @staticmethod
    def __normalize_text(text):
        normalized = unicodedata.normalize('NFKD', text)
        no_nikkud = ''.join([c for c in normalized if not unicodedata.combining(c)])
        return no_nikkud

    @staticmethod
    def __is_valid_search_results(search_results):
        if 'SearchResults' not in search_results:
            return False

        if search_results['SearchResults'] is None:
            return False

        if search_results['SearchResults']['items'] is None:
            return False

        return True

    @staticmethod
    def __used_spelling(data):
        try:
            return data['SearchResults']['spelling'] is not None
        except:
            return False

    def __get_items_by_search_word(self, search_word):
        items = []
        page_number = 1
        no_more_results = False

        while not no_more_results:
            with requests.Session() as session:
                response = session.get(url=self._search_word_url.format(search_word, page_number))
                data = json.loads(ast.literal_eval(response.content))

                if self.__is_valid_search_results(data):
                    used_spelling = self.__used_spelling(data)
                    item = {'UsedSpelling': used_spelling}
                    if used_spelling:
                        item['Suggested'] = data['SearchResults']['spelling']['correctedQuery'].encode('utf-8')
                    else:
                        item['Suggested'] = None
                    item['Items'] = data['SearchResults']['items']

                    items.append(item)
                else:
                    no_more_results = True

            page_number += 1
        return items
