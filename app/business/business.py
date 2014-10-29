from app.data.data import Data

### Business logic to communicate and process data instances ###
class BusinessLogic(object):
    data = Data()

    def product_list(self):
        return self.data['products']

    def product_information(self, product):
        return self.data['products'].get(product, None)



