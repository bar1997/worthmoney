# -*- coding: utf-8 -*-
from flask import Blueprint
from Models.APIs.IsracardCorporation.IsracardGroup import IsracardGroup

BLUEPRINT = Blueprint(__name__, '', url_prefix='/AmericanExpress')


class AmericanExpressFingerprint(IsracardGroup):
    def __init__(self):
        raise NotImplementedError('')

    @staticmethod
    @BLUEPRINT.after_request
    def after_request(response):
        header = response.headers
        header['Access-Control-Allow-Origin'] = '*'
        header['Access-Control-Allow-Headers'] = '*'
        return response
