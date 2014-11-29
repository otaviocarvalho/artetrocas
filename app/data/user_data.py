list_users = {
    0: {'name': 'admin', 'full_name': 'Admin admin', 'wallet': 100},
    1: {'name': 'test', 'full_name': 'Test tester', 'wallet': 150},
    2: {'name': 'otavio', 'full_name': 'Otavio Carvalho', 'wallet': 300},
}

class UserData(object):
    class __UserData:
        def __init__(self):
            self.list_users = list_users

        def get_users(self):
            return self.list_users

        def get_users_clean(self, user_id):
            dict_aux = dict(self.list_users)
            del dict_aux[user_id]
            return dict_aux

        def get_user_key(self, keyword):
            users_list_aux = {}
            for key,value in self.list_users.iteritems():
                # Search by names
                if (value['name'].lower() == keyword.lower()):
                    users_list_aux[key] = value

            return users_list_aux

        def get_user_id(self, user_id):
            users_list_aux = {}
            for key,value in self.list_users.iteritems():
                # Search by names
                if (key == user_id):
                    users_list_aux[key] = value

            return users_list_aux

    instance = None
    def __new__(cls):
        if not UserData.instance:
            UserData.instance = UserData.__UserData()
        return UserData.instance



