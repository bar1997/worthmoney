class Coupon(object):
    def __init__(self, title, description, link, corporation, price=None):
        self.__title = title
        self.__description = description
        self.__link = link
        self.__corporation = corporation
        self.__price = price

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_link(self):
        return self.__link

    def get_price(self):
        return self.__price

    def get_corporation(self):
        return self.__corporation

    def to_json(self):
        json_coupon = dict()

        json_coupon['Title'] = self.__title
        json_coupon['Description'] = self.__description
        json_coupon['Price'] = self.__price
        json_coupon['Link'] = self.__link
        json_coupon['Corporation'] = self.__corporation

        return json_coupon
