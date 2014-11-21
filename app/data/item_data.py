items = {
    0: { 'title': 'Mondrian', 'school': 'Neoplasticismo', 'quantity': 10, 'user_id': 1 },
    1: { 'title': 'Picasso', 'school': 'Cubismo', 'quantity': 100, 'user_id': 1 },
    2: { 'title': 'Renoir', 'school': 'Impressionismo', 'quantity': 10, 'user_id': 2 },
    3: { 'title': 'Monet', 'school': 'Impressionismo', 'quantity': 20, 'user_id': 2 }
}

class ItemData(object):
    class __ItemData:
        def __init__(self):
            self.items = items

        def get_items(self):
            return self.items

        def get_item_key(self, keyword):
            items_list = {}
            for key,value in self.items.iteritems():
                # Search by names
                #if (value['title'].lower() == keyword.lower()):
                if value['title'].lower().find(keyword.lower()) != -1:
                    items_list[key] = value
                # Search by school
                elif value['school'].lower().find(keyword.lower()) != -1:
                    items_list[key] = value

            return items_list

        def get_items_user(self, user_id):
            items_list = {}
            for key,value in self.items.iteritems():
                if value['user_id'] == user_id:
                    items_list[key] = value

            return items_list


    instance = None
    def __new__(cls):
        if not ItemData.instance:
            ItemData.instance = ItemData.__ItemData()
        return ItemData.instance

