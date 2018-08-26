# -*- coding: utf-8 -*-
import json
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

            page_number += 1

        filtered = 0
        for items in all_items:
            for item in items:
                description = item['htmlSnippet'].encode('utf-8')
                title = item['htmlTitle'].encode('utf-8')
                link = item['link'].encode('utf-8')

                if user_input in description or user_input in title:
                    print 'Description: ' + description
                    print 'Title: ' + title
                    print 'Link: ' + link
                    print '---'
                    filtered += 1

        print str.format('Found {0} results', filtered)


