import random

list_items = {
    0: { 'title': 'Mondrian', 'school': 'Neoplasticismo', 'quantity': 10, 'user_id': 1 },
    1: { 'title': 'Picasso', 'school': 'Cubismo', 'quantity': 100, 'user_id': 1 },
    2: { 'title': 'Renoir', 'school': 'Impressionismo', 'quantity': 10, 'user_id': 2 },
    3: { 'title': 'Monet', 'school': 'Impressionismo', 'quantity': 20, 'user_id': 2 }
}

class ItemData(object):
    class __ItemData:
        def __init__(self):
            self.list_items = list_items

        def set_item(self, key, item):
            if key in list_items.keys():
                list_items[key] = item

        def set_item_quantity(self, key, quantity):
            if key in list_items.keys():
                list_items[key]['quantity'] = quantity

        def get_item(self, item_id):
            return self.list_items.get(item_id)

        def get_items(self):
            return self.list_items

        def get_item_key(self, keyword):
            items_list_aux = {}
            for key,value in self.list_items.iteritems():
                # Search by names
                if value['title'].lower().find(keyword.lower()) != -1:
                    items_list_aux[key] = value
                # Search by school
                elif value['school'].lower().find(keyword.lower()) != -1:
                    items_list_aux[key] = value

            return items_list_aux

        def get_items_user(self, user_id):
            items_list_aux = {}
            for key,value in self.list_items.iteritems():
                if value['user_id'] == user_id:
                    items_list_aux[key] = value

            return items_list_aux

        def set_item_user(self, key, user_id):
            if not key in self.list_items:
                self.list_items[key] = { 'title': 'empty', 'school': 'empty', 'quantity': 0, 'user_id': user_id }
                return { key: self.list_items[key] }
            else:
                return None

        def create_item_user(self, user_id):
            greater_key = -1
            for key in self.list_items.keys():
                if key > greater_key:
                    greater_key = key

            item = self.set_item_user(greater_key+1, user_id)
            return item

        def insert_item(self, item):
            for key in item.keys():
                self.list_items[key] = item[key]

        def insert_new_item(self, item):
            # Procura uma chave que ainda nao esteja no dicionario
            new_key = random.randrange(10000, 99999)
            while new_key in self.list_items.keys():
                new_key = random.randrange(10000, 99999)

            self.list_items[new_key] = item

    # Gerencia do Singleton em Python
    instance = None
    def __new__(cls):
        if not ItemData.instance:
            ItemData.instance = ItemData.__ItemData()
        return ItemData.instance

class Item(object):
    def __init__(self, item_id, title, school, quantity, user_id):
        self.item_id = item_id
        self.title = title
        self.school = school
        self.quantity = quantity
        self.user_id = user_id

    def commit(self, list_items):
        dict_items = { 'title': self.title, 'school': self.school, 'quantity': self.quantity, 'user_id': self.user_id }
        #print dict_items
        list_items[self.item_id] = dict_items
        return list_items
