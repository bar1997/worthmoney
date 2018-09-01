# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod


class CouponSite(object):
    __metaclass__ = ABCMeta

    def __init__(self, search_url):
        self._coupons = []
        self._search_word_url = search_url

    @abstractmethod
    def get_coupons_by_word(self, word):
        """
        :param word: String to search in site
        :return: list of filters Coupons
        """
        pass
