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

    #@staticmethod
    #@BLUEPRINT.route('/GetHeverInfo', methods=['POST'])
    #def get_isracard_info():
    #    return Response.succeed_response(None)

    @staticmethod
    def write_file(text):
        with open('C:\\Users\\Bar\\AppData\\Local\\Temp\\temp.html', 'wb') as file_handle:
            file_handle.write(text)

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

        while not no_more_results:
            with requests.Session() as session:
                response = session.get(url=Isracard.ISRACARD_SEARCH_WORD.format(user_input, page_number))
                data = json.loads(ast.literal_eval(response.content))
                no_more_results = data['SearchResults'] is None

                if not no_more_results:
                    all_items.append(data['SearchResults']['items'])

                    print str.format('Found {0} items on page {1}', len(data['SearchResults']['items']), page_number)

            page_number += 1

        filtered = 0
        for items in all_items:
            for item in items:
                try:
                    description = Isracard.normalize_text(item['snippet'])
                    title = Isracard.normalize_text(item['title']).encode('utf-8')
                    link = Isracard.normalize_text(item['link']).encode('utf-8')

                    # print str.format('In title ({0}): {1}', title, user_input in title)

                    import chardet
                    print chardet.detect(user_input)['encoding']
                    #print chardet.detect(description)['encoding']
                    print description.decode('utf-8')


                    print str.format('In description ({0}): {1}', description, user_input in description.encode('utf-8').encode('latin1'))
                    print ''

                    '''
                    if (user_input in description or user_input in title) and 'ההטבה הסתיימה' not in title:
                        print 'Description: ' + description
                        print 'Title: ' + title
                        print 'Link: ' + link
                        print '---'
                        filtered += 1
                    '''

                except Exception as daniella:
                    print str(daniella)
                    import sys
                    sys.exit(-1)

        print str.format('Found {0} results', filtered)


