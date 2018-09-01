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
    def __get_coupons(word):
        corporations = list()
        corporations.append(AmericanExpress())
        corporations.append(Isracard())

        coupons = CouponsProvider.__get_coupons_from_corporations(corporations, word)

        return coupons

    @staticmethod
    def get_coupons(word):
        return CouponsProvider.__get_coupons(word)

    @staticmethod
    def get_coupons_as_json(word, selected_corporations):
        coupons = CouponsProvider.__get_coupons(word)
        results = list()

        for coupon in coupons:
            if coupon.get_corporation() in selected_corporations:
                results.append(coupon.to_json())

        return results
