users = {
    'admin': {'full_name': 'Admin admin', 'wallet': 100},
    'test': {'full_name': 'Test tester', 'wallet': 150},
    'otavio': {'full_name': 'Otavio Carvalho', 'wallet': 300},
}

class UserData(object):
    def __init__(self):
        self.users = users

    def get_users(self):
        return self.users

    def get_user_key(self, keyword):
        users_list = {}
        for key,value in self.users.iteritems():
            # Search by names
            if (key.lower() == keyword.lower()):
                users_list[key] = value

        return users_list



