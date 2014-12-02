import random

list_items = {
    0: {
        'title': 'Boogie-Woogie',
        'author': 'Mondrian',
        'description': 'Boogie-Woogie e um quadro de Piet Mondrian, completado em 1943, pouco depois de este se ter mudado para Nova Iorque, em 1940.',
        'school': 'Neoplasticismo',
        'type': 'Pintura a Oleo',
        'quantity': 10,
        'user_id': 1
    },
    1: {
        'title': 'Picasso',
        'author': 'Picasso',
        'description': 'Picasso',
        'school': 'Cubismo',
        'type': 'Pintura a Oleo',
        'quantity': 100,
        'user_id': 1
    },
    2: {
        'title': 'Renoir',
        'author': 'Renoir',
        'description': 'Renoir',
        'school': 'Impressionismo',
        'type': 'Pintura a Oleo',
        'quantity': 10,
        'user_id': 2
    },
    3: {
        'title': 'Monet',
        'author': 'Monet',
        'description': 'Monet',
        'school': 'Impressionismo',
        'type': 'Pintura a Oleo',
        'quantity': 20,
        'user_id': 2
    }
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

        def convert_dict_to_item(self, item_key, item_dict):
            item = Item(item_key)

            item.key = item_key
            item.title = item_dict['title']
            item.author = item_dict['author']
            item.description = item_dict['description']
            item.school = item_dict['school']
            item.type_item = item_dict['type']
            item.quantity = item_dict['quantity']
            item.user_id = item_dict['user_id']

            return item

        def get_item(self, item_id):
            print self.list_items[item_id]
            item = self.convert_dict_to_item(item_id, self.list_items[item_id])
            #return self.list_items.get(item_id)
            return item

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

        #def set_item_user(self, key, user_id):
            #if not key in self.list_items:
                #self.list_items[key] = {
                                        #'title': 'empty',
                                        #'author': 'empty',
                                        #'description': 'empty',
                                        #'school': 'empty',
                                        #'type': 'empty',
                                        #'quantity': 0,
                                        #'user_id': user_id
                                       #}
                #return { key: self.list_items[key] }
            #else:
        #        return None

        def create_item_user(self, user_id):
            greater_key = -1
            for key in self.list_items.keys():
                if key > greater_key:
                    greater_key = key

            #item = self.set_item_user(greater_key+1, user_id)
            item = Item()
            item.user_id = user_id
            return item

        def generate_key(self):
            # Procura uma chave que ainda nao esteja no dicionario
            new_key = random.randrange(10000, 99999)
            while new_key in self.list_items.keys():
                new_key = random.randrange(10000, 99999)

            return new_key

        def insert_item(self, item):
            item_dict = self.convert_item_to_dict(item)
            self.list_items[item.key] = item_dict

            return True

        def insert_new_item(self, item):
            key = generate_key()
            item_dict = self.convert_item_to_dict(item)
            self.list_items[item.key] = item_dict
            #for key in item.keys():
                #self.list_items[key] = item[key]

            return True

        def convert_item_to_dict(self, item):
            # Cria um novo dicionario
            new_dict = {
                            'title': item.title,
                            'author': item.author,
                            'description': item.description,
                            'school': item.school,
                            'type': item.type,
                            'quantity': item.quantity,
                            'user_id': item.user_id
                       }

            return { item.key : new_dict }

    # Gerencia do Singleton em Python
    instance = None
    def __new__(cls):
        if not ItemData.instance:
            ItemData.instance = ItemData.__ItemData()
        return ItemData.instance

class Item(object):
    def __init__(self, key=-1, title="", author=None, description=None, school=None, type_item=None, quantity=-1, user_id=-1):
        self.key = key
        self.title = title
        self.author = author
        self.description = description
        self.school = school
        self.type = type_item
        self.quantity = quantity
        self.user_id = user_id
