# -*- coding: utf-8 -*-

from Models.APIs.IsracardGroup.AmericanExpress import AmericanExpress


def main():
    american = AmericanExpress()
    word = raw_input('enter word: ')
    lst = american.get_coupons_by_word(word)
    for i in lst:
        i.print_info()
    # Server.start(WebConfigurations.SERVER_PORT)
    # user_input = raw_input('Enter your input:')
    # Isracard.get_coupons_by_input(user_input)
    # AmericanExpress.get_coupons_by_input(user_input)
    #Discount.get_coupons_by_input()

if '__main__' == __name__:
    main()
