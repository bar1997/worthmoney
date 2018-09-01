class Coupon(object):
    def __init__(self, title, description, link, price=None):
        self.__title = title
        self.__description = description
        self.__link = link
        self.__price = price

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_link(self):
        return self.__link

    def get_price(self):
        return self.__price

    def print_info(self):
        print 'Title: ' + self.__title
        print 'Description: ' + self.__description
        print 'Link: ' + self.__link

        if self.__price:
            print 'Price: ' + self.__price

        print '*********************'
