from app.data.item_data import ItemData
from app.data.user_data import UserData

class ItemBusiness(object):
    item_data = ItemData()
    user_data = UserData()

    def get_item(self, item_id):
        item = self.item_data.get_item(item_id)

        #print "user_id"
        #print item["user_id"]
        #print self.user_data.get_user_id(item["user_id"]).get(item["user_id"])
        # Add item id and owner to query answer
        if item:
            item["id"] = item_id
            item["owner"] = (self.user_data.get_user_id(item["user_id"])).get(item["user_id"]).get("full_name")

        return self.item_data.get_item(item_id)

    def items_list(self):
        return self.item_data.get_items()

    def items_list_key(self, keyword):
        return self.item_data.get_item_key(keyword)
