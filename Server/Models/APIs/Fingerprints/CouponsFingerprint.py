# -*- coding: utf-8 -*-
from flask import Blueprint, request
from Models.Response import Response
from Models.APIs.IsracardCorporation.IsracardGroup import IsracardGroup
from Models.CouponsProvider import CouponsProvider
from Models.Validation import Validation

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
            validation = Validation(request.json)

            if not validation.keys_exists(keys=['UserInput', 'Corporations']):
                return Response.failed_response(validation.get_last_message())

            if validation.are_keys_none(keys=['UserInput', 'Corporations']):
                return Response.failed_response(validation.get_last_message())

            if not validation.is_valid_type(keys=['UserInput'], key_type=unicode):
                return Response.failed_response(validation.get_last_message())

            if not validation.is_valid_type(keys=['Corporations'], key_type=list):
                return Response.failed_response(validation.get_last_message())

            if validation.is_list_contains_none(key='Corporations'):
                return Response.failed_response(validation.get_last_message())

            if not validation.is_list_items_same_type(key='Corporations', key_type=unicode):
                return Response.failed_response(validation.get_last_message())

            if validation.is_list_contains_empty_string(key='Corporations'):
                return Response.failed_response(validation.get_last_message())

            user_input = request.json['UserInput'].encode('utf-8')
            selected_corporations = request.json['Corporations']

            coupons_json = CouponsProvider.get_coupons_as_json(user_input, selected_corporations)

            return Response.succeed_response(coupons_json)
        except Exception as e:
            print 'get_coupons_from_selected_corporations'
            print str(e)
