from app.data.data import Data

class SearchBusiness(object):
    data = Data()

    def items_list(self):
        #return self.data['items']
        return self.data.get_items()

    def items_list_key(self, keyword):
        data_test = Data()
        return self.data.get_item_key(keyword)
