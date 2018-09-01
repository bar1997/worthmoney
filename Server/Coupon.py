class Coupon(object):
    def __init__(self, title, description, link):
        self.title = title
        self.description = description
        self.link = link

    def print_info(self):
        print "Title: " + self.title
        print "Description: " + self.description
        print "Link: " + self.link
        print "*********************"
