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

        def convert_dict_to_item(self, item_dict, item_key=None):
            if item_key is None:
                item = Item()
                item_key = item_dict.keys()[0]
                item_dict = item_dict[item_key]
            else:
                item = Item(item_key)

            item.key = item_key
            item.title = item_dict['title']
            item.author = item_dict['author']
            item.description = item_dict['description']
            item.school = item_dict['school']
            item.type = item_dict['type']
            item.quantity = item_dict['quantity']
            item.user_id = item_dict['user_id']

            return item

        def get_item(self, item_id):
            #print self.list_items[item_id]
            item = self.convert_dict_to_item(self.list_items[item_id], item_id)
            #return self.list_items.get(item_id)
            return item

        def get_items(self):
            # Montar lista de objetos
            list_aux = []
            #print self.list_items
            for item_key in self.list_items.keys():
                #print self.list_items[item_key]
                list_aux.append(self.convert_dict_to_item(self.list_items[item_key], item_key))

            #return self.list_items
            return list_aux

        def get_item_key(self, keyword):
            items_list = self.get_items()
            items_list_aux = []
            for item in items_list:
                print item.title
                print item.type
                # Procurar por nome
                if item.title.lower().find(keyword.lower()) != -1:
                    items_list_aux.append(item)
                # Procurar por autor
                if item.author.lower().find(keyword.lower()) != -1:
                    items_list_aux.append(item)
                # Procurar por tipo
                if item.type.lower().find(keyword.lower()) != -1:
                    items_list_aux.append(item)

            #for key,value in self.list_items.iteritems():
                ## Search by names
                #if value['title'].lower().find(keyword.lower()) != -1:
                    #items_list_aux[key] = value
                ## Search by school
                #elif value['school'].lower().find(keyword.lower()) != -1:
                    #items_list_aux[key] = value

            return items_list_aux

        def get_items_user(self, user_id):
            # Montar lista de objetos
            list_aux = []
            for item_key in self.list_items.keys():
                if item_key == user_id:
                    list_aux.append(self.convert_dict_to_item(self.list_items[item_key], item_key))

            return list_aux

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
            self.list_items[item.key] = item_dict[item.key]

            return True

        def insert_new_item(self, item):
            item.key = self.generate_key()
            print item.key
            item_dict = self.convert_item_to_dict(item)
            print item_dict
            self.list_items[item.key] = item_dict[item.key]
            print self.list_items
            #for key in item.keys():
                #self.list_items[key] = item[key]

            return True

    # Gerencia do Singleton em Python
    instance = None
    def __new__(cls):
        if not ItemData.instance:
            ItemData.instance = ItemData.__ItemData()
        return ItemData.instance

class Item(object):
    def __init__(self, key=-1, title="", author="", description="", school="", type_item="", quantity=-1, user_id=-1):
        self.key = key
        self.title = title
        self.author = author
        self.description = description
        self.school = school
        self.type = type_item
        self.quantity = quantity
        self.user_id = user_id
