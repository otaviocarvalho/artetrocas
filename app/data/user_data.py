users = {
    0: {'name': 'admin', 'full_name': 'Admin admin', 'wallet': 100},
    1: {'name': 'test', 'full_name': 'Test tester', 'wallet': 150},
    2: {'name': 'otavio', 'full_name': 'Otavio Carvalho', 'wallet': 300},
}

class UserData(object):
    def __init__(self):
        self.users = users

    def get_users(self):
        return self.users

    def get_users_clean(self, user_id):
        dict_aux = dict(self.users)
        del dict_aux[user_id]
        return dict_aux

    def get_user_key(self, keyword):
        users_list = {}
        for key,value in self.users.iteritems():
            # Search by names
            if (value['name'].lower() == keyword.lower()):
                users_list[key] = value

        return users_list

    def get_user_id(self, user_id):
        users_list = {}
        for key,value in self.users.iteritems():
            # Search by names
            if (key == user_id):
                users_list[key] = value

        return users_list




