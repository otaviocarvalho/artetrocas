from app.data.user_data import UserData
from app.data.item_data import ItemData

class UserBusiness(object):
    user_data = UserData()
    item_data = ItemData()

    def users_list(self):
        return self.user_data.get_users()

    def users_list_key(self, keyword):
        return self.transaction_data.get_user_key(keyword)

    def get_user_items(self, user):
        return self.item_data.get_items_user(user)

    def get_users_exchange_items(self, ids, qtds):
        # Get users based on the items they have
        # self.item_data
        return self.user_data.get_users()
