from app.data.data import Data

class BusinessLogic(object):
    """ Business logic holding data store instances """
    data = Data()
    print "business logic py"

    def product_list(self):
        return self.data['products'].keys()

    def product_information(self, product):
        return self.data['products'].get(product, None)



