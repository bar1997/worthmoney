# -*- coding: utf-8 -*-
from Models.CouponsProvider import CouponsProvider


def main():
    word = raw_input('Enter word: ')
    coupons = CouponsProvider.get_coupons(word)

    for coupon in coupons:
        coupon.print_info()

    # Server.start(WebConfigurations.SERVER_PORT)
    # user_input = raw_input('Enter your input:')
    # Isracard.get_coupons_by_input(user_input)
    # AmericanExpress.get_coupons_by_input(user_input)
    #Discount.get_coupons_by_input()

if '__main__' == __name__:
    main()
