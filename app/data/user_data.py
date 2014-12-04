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
            list_aux = []
            for user_key in self.list_users.keys():
                list_aux.append(self.convert_dict_to_user(self.list_users[user_key], user_key))

            return list_aux
            #return self.list_users

        def get_users_clean(self, user_id):
            list_aux = []
            for user_key in self.list_users.keys():
                if user_key != user_id:
                    list_aux.append(self.convert_dict_to_user(self.list_users[user_key], user_key))

            return list_aux
            #dict_aux = dict(self.list_users)
            #del dict_aux[user_id]
            #return dict_aux

        def get_user_key(self, keyword):
            list_aux = []
            for user_key in self.list_users.keys():
                user_aux = self.convert_dict_to_user(self.list_users[user_key], user_key)
                if user_aux.name.lower() == keyword.lower():
                    list_aux.append(user_aux)

            return list_aux
            #users_list_aux = {}
            #for key,value in self.list_users.iteritems():
                # Search by names
                #if (value['name'].lower() == keyword.lower()):
                    #users_list_aux[key] = value
            #return users_list_aux

        def get_user_id(self, user_id):
            list_aux = []
            for user_key in self.list_users.keys():
                user_aux = self.convert_dict_to_user(self.list_users[user_key], user_key)
                if user_aux.key == user_id:
                    return user_aux

            return None
            #users_list_aux = {}
            #for key,value in self.list_users.iteritems():
                # Search by names
                #if (key == user_id):
                    #users_list_aux[key] = value
            #return users_list_aux

        def insert_user(self, user):
            user_dict = self.convert_user_to_dict(user)
            self.list_users[user.key] = user_dict[user.key]

            return True

        def insert_new_user(self, user):
            user.key = self.generate_key()
            user_dict = self.convert_user_to_dict(user)
            self.list_users[user.key] = user_dict[user.key]

            return True

        def generate_key(self):
            # Procura uma chave que ainda nao esteja no dicionario
            new_key = random.randrange(10000, 99999)
            while new_key in self.list_users.keys():
                new_key = random.randrange(10000, 99999)

            return new_key

        def convert_user_to_dict(self, user):
            # Cria um novo dicionario
            new_dict = {
                            'name': user.name,
                            'full_name': user.full_name,
                            'wallet': user.wallet
                       }

            return { user.key : new_dict }

        def convert_dict_to_user(self, user_dict, user_key=None):
            if user_key is None:
                user = User()
                user_key = user_dict.keys()[0]
                user_dict = user_dict[user_key]
            else:
                user = User(user_key)

            user.key = user_key
            user.name = user_dict['name']
            user.full_name = user_dict['full_name']
            user.wallet = user_dict['wallet']

            return user

    instance = None
    def __new__(cls):
        if not UserData.instance:
            UserData.instance = UserData.__UserData()
        return UserData.instance

class User(object):
    def __init__(self, key=-1, name="", full_name="", wallet=0, products=[], quantities=[]):
        self.key = key
        self.name = name
        self.full_name = full_name
        self.wallet = wallet
        self.products = products
        self.quantities = quantities
