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
    def test():
        user_input = raw_input('Search:')

        all_items = []
        page_number = 1
        no_more_results = False

        suggested_word = None

        while not no_more_results:
            with requests.Session() as session:
                response = session.get(url=Isracard.ISRACARD_SEARCH_WORD.format(user_input, page_number))
                data = json.loads(ast.literal_eval(response.content))

                if 'SearchResults' in data.keys():
                    no_more_results = data['SearchResults'] is None
                    if not no_more_results:
                        should_be_correct = data['SearchResults']['spelling'] is not None
                        if should_be_correct:
                            suggested_word = data['SearchResults']['spelling']['correctedQuery'].encode('utf-8')
                            print str.format('Corrected to {0}', user_input)

                        if data['SearchResults']['items'] is not None:
                            all_items.append(data['SearchResults']['items'])
                            print data['SearchResults']['items']
                            print str.format('Found {0} items on page {1}', len(data['SearchResults']['items']), page_number)
                else:
                    no_more_results = True

            page_number += 1

        filtered = 0
        for items in all_items:
            for item in items:
                description = Isracard.normalize_text(item['snippet']).encode('utf-8')
                title = Isracard.normalize_text(item['title']).encode('utf-8')
                link = Isracard.normalize_text(item['link']).encode('utf-8')

                if suggested_word is None:
                    if user_input in title or user_input in description:
                        print 'Description: ' + description
                        print 'Title: ' + title
                        print 'Link: ' + link
                        print '---'
                        filtered += 1
                else:
                    if (suggested_word in title) or (suggested_word in description) or (user_input in title) or (user_input in description):
                        print 'Description: ' + description
                        print 'Title: ' + title
                        print 'Link: ' + link
                        print '---'
                        filtered += 1

        print str.format('Found {0} results', filtered)


