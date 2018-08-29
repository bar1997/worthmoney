from Configurations.WebConfigurations import WebConfigurations
from Models.Server import Server
from Models.APIs.Hever import Hever
from Models.APIs.Isracard import Isracard
from Models.APIs.AmericanExpress import AmericanExpress
from Models.APIs.Discount import Discount


def main():
    # Server.start(WebConfigurations.SERVER_PORT)
    # user_input = raw_input('Enter your input:')
    # Isracard.get_coupons_by_input(user_input)
    # AmericanExpress.get_coupons_by_input(user_input)
    Discount.get_coupons_by_input()

if '__main__' == __name__:
    main()
