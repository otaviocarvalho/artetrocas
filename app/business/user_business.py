from app.data.user_data import UserData
from app.data.item_data import ItemData

import copy

class UserBusiness(object):
    user_data = UserData()
    item_data = ItemData()

    def users_list(self):
        return self.user_data.get_users()

    # User list without session user
    def users_list_clean(self, user_id):
        return self.user_data.get_users_clean(user_id)

    def users_list_key(self, keyword):
        return self.user_data.get_user_key(keyword)

    def get_user_items(self, user):
        return self.item_data.get_items_user(user)

    def get_user_id(self, user_id):
        return self.user_data.get_user_id(user_id)

    def get_users_exchange_items(self, ids, qtds, my_user_id):
        # Get users based on the items they have
        #list_users = self.user_data.get_users_clean(my_user_id)
        #print list_users
        ## Get list of items per user
        #for key_user,value_user in list_users.iteritems():
            #list_items = self.item_data.get_items_user(key_user)
            ##print list_items
            #for key_item, value_item in list_items.iteritems():
                #if not 'products' in list_users[key_user]:
                    #list_users[key_user]['products'] = [ key_item ]
                    #list_users[key_user]['quantities'] = [ value_item['quantity'] ]
                #else:
                    #list_users[key_user]['products'].append(key_item)
                    #list_users[key_user]['quantities'].append(value_item['quantity'])
        #return list_users
        # Cria copia dos usuarios do sistema
        list_users = copy.deepcopy(self.user_data.get_users_clean(my_user_id))
        for user in list_users:
            # Pega os itens de cada usuario do sistema
            list_items = self.item_data.get_items_user(user.key)

            list_user_products = []
            list_user_quantities = []
            # Cria lista de itens e quantidades por usuario
            for item in list_items:
                list_user_products.append(item.key)
                list_user_quantities.append(item.quantity)

            # Adiciona lista de itens e quantidades ao objeto do usuario na lista
            user.products = list_user_products
            user.quantities = list_user_quantities

        return list_users


