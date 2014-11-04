#from app.data.data import Data
from app.data.item_data import ItemData

class SearchBusiness(object):
    #data = Data()
    item_data = ItemData()

    def items_list(self):
        return self.item_data.get_items()

    def items_list_key(self, keyword):
        return self.item_data.get_item_key(keyword)
