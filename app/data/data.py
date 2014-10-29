### Data Store Class
class Data(object):
    """ Data Store Class """

    products = {
        'Mondrian': {'school': 'Neoplasticism', 'quantity': 10},
        'Picasso': {'school': 'Cubism', 'quantity': 100},
        'Renoir': {'school': 'Impressionism', 'quantity': 10}
    }

    def __get__(self, obj, klas):
        print ("(Fetching from Data Store)")
        return {'products': self.products}



