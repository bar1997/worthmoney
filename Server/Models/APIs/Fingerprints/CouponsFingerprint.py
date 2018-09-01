# -*- coding: utf-8 -*-
from flask import Blueprint, request
from Models.Response import Response
from Models.APIs.IsracardCorporation.IsracardGroup import IsracardGroup
from Models.CouponsProvider import CouponsProvider

BLUEPRINT = Blueprint(__name__, '', url_prefix='/Coupons')


class CouponsFingerprint(IsracardGroup):
    def __init__(self):
        raise NotImplementedError('')

    @staticmethod
    @BLUEPRINT.after_request
    def after_request(response):
        header = response.headers
        header['Access-Control-Allow-Origin'] = '*'
        header['Access-Control-Allow-Headers'] = '*'
        return response

    @staticmethod
    @BLUEPRINT.route('/GetCouponsFromSelectedCorporations', methods=['POST'])
    def get_coupons_from_selected_corporations():
        try:
            user_input = request.json['UserInput'].encode('utf-8')
            selected_corporations = request.json['Corporations']

            return Response.succeed_response(CouponsProvider.get_coupons_as_json(user_input, selected_corporations))
        except Exception as e:
            print 'get_coupons_from_selected_corporations'
            print str(e)
