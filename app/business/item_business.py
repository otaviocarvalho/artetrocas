from app.data.item_data import ItemData
from app.data.user_data import UserData

class ItemBusiness(object):
    item_data = ItemData()
    user_data = UserData()

    def get_item(self, item_id):
        item = self.item_data.get_item(item_id)

        # Adiciona o id do item e o proprietario a resposta
        if item is not None:
            user = self.user_data.get_user_id(item.user_id)
            item.owner = user.full_name

        return item

    def items_list(self):
        return self.item_data.get_items()

    def items_list_key(self, keyword):
        return self.item_data.get_item_key(keyword)

    def create_item(self, user_id):
        return self.item_data.create_item_user(user_id)

    def insert_item(self, item):
        return self.item_data.insert_item(item)

    def insert_new_item(self, item):
        return self.item_data.insert_new_item(item)
