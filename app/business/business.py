from app.data.data import Data

class Business(object):
    data = Data()

    def items_list(self):
        return self.data.get_items()
        #return self.data['items']
