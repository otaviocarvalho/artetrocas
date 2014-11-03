from app.data.user_data import UserData

class UserBusiness(object):
    user_data = UserData()

    def users_list(self):
        return self.user_data.get_users()

    def users_list_key(self, keyword):
        return self.transaction_data.get_user_key(keyword)
