class Data(object):
    """ Data Store Class """

    print "data py"

    products = {
        'milk': {'price': 1.50, 'quantity': 10},
        'eggs': {'price': 0.20, 'quantity': 100},
        'cheese': {'price': 2.00, 'quantity': 10}
    }

    def __get__(self, obj, klas):
        print ("(Fetching from Data Store)")
        return {'products': self.products}



