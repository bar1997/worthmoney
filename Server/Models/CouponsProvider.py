from Models.APIs.IsracardCorporation.AmericanExpress import AmericanExpress
from Models.APIs.IsracardCorporation.Isracard import Isracard


class CouponsProvider (object):
    def __init__(self):
        raise NotImplementedError('')

    @staticmethod
    def __get_coupons_from_corporations(corporations, word):
        coupons = list()

        for corporation in corporations:
            coupons.extend(corporation.get_coupons_by_word(word))

        return coupons

    @staticmethod
    def get_coupons(word):
        corporations = list()
        corporations.append(AmericanExpress())
        corporations.append(Isracard())

        coupons = CouponsProvider.__get_coupons_from_corporations(corporations, word)

        return coupons