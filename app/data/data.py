items = {
    'Mondrian': {'school': 'Neoplasticism', 'quantity': 10},
    'Picasso': {'school': 'Cubism', 'quantity': 100},
    'Renoir': {'school': 'Impressionism', 'quantity': 10},
    'Monet': {'school': 'Impressionism', 'quantity': 5}
}

class Data(object):
    class __Data:
        def __init__(self):
            self.items = items

        def get_items(self):
            return self.items

        def get_item_key(self, keyword):
            items_list = {}
            for key,value in self.items.iteritems():
                # Search by names
                if (key.lower() == keyword.lower()):
                    items_list[key] = value
                # Search by school
                elif (value['school'].lower() == keyword.lower()):
                    items_list[key] = value

            return items_list

    instance = None
    def __new__(cls):
        if not Data.instance:
            Data.instance = Data.__Data()
        return Data.instance

