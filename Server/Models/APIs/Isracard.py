# -*- coding: utf-8 -*-
import json
import unicodedata
import ast
import requests
from Models.Response import Response
from flask import Blueprint

BLUEPRINT = Blueprint(__name__, '', url_prefix='/Hever')


class Isracard(object):
    ISRACARD_SEARCH_WORD = 'https://digital.isracard.co.il/SearchResult/Search?query={0}&actionType=new&startPage={1}&inurl=all&siteName=isracard'

    def __init__(self):
        raise NotImplementedError('')

    @staticmethod
    @BLUEPRINT.route('/GetHeverInfo', methods=['POST'])
    def get_isracard_info():
        return Response.succeed_response(None)

    @staticmethod
    def normalize_text(text):
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

    @staticmethod
    def __get_items_by_search_word(search_word):
        items = []
        page_number = 1
        no_more_results = False

        while not no_more_results:
            with requests.Session() as session:
                response = session.get(url=Isracard.ISRACARD_SEARCH_WORD.format(search_word, page_number))
                data = json.loads(ast.literal_eval(response.content))

                if Isracard.__is_valid_search_results(data):
                    used_spelling = Isracard.__used_spelling(data)
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

    @staticmethod
    def get_coupons_by_input(user_input):
        items = Isracard.__get_items_by_search_word(user_input)

        filtered = 0
        for page_items in items:
            for item in page_items['Items']:
                description = Isracard.normalize_text(item['snippet']).encode('utf-8')
                title = Isracard.normalize_text(item['title']).encode('utf-8')
                link = Isracard.normalize_text(item['link']).encode('utf-8')

                forbidden_postfix = 'ההטבה הסתיימה'
                user_input_in_search_results = user_input in title or user_input in description

                if page_items['UsedSpelling']:
                    suggested_in_search_results = page_items['Suggested'] in title or page_items['Suggested'] in description

                    if (forbidden_postfix not in title) and (suggested_in_search_results or user_input_in_search_results):
                        # print 'Description: ' + description
                        # print 'Title: ' + title
                        # print 'Link: ' + link
                        # print 'Used spelling: ' + str(page_items['UsedSpelling'])
                        # print 'Suggested word: ' + str(page_items['Suggested'])
                        # print '---'
                        filtered += 1
                else:
                    if (forbidden_postfix not in title) and user_input_in_search_results:
                        # print 'Description: ' + description
                        # print 'Title: ' + title
                        # print 'Link: ' + link
                        # print '---'
                        filtered += 1

