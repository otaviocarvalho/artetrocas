transactions = {
    '12345': {'user_from': 'test', 'user_to': 'otavio', 'list_items': {'Mondrian', 'Picasso', 'Renoir'} },
    '12346': {'user_from': 'test', 'user_to': 'otavio', 'list_items': {'Mondrian', 'Picasso', 'Renoir'} },
    '12347': {'user_from': 'test', 'user_to': 'otavio', 'list_items': {'Mondrian', 'Picasso', 'Renoir'} },
    '54321': {'user_from': 'otavio', 'user_to': 'test', 'list_items': {'Mondrian'} },
    '53321': {'user_from': 'otavio', 'user_to': 'test', 'list_items': {'Mondrian'} }
}

class TransactionData(object):
    def __init__(self):
        self.transactions = transactions

    def get_transactions(self):
        return self.transactions

    def get_transaction_key(self, keyword):
        transactions_list = {}
        for key,value in self.transactions.iteritems():
            # Search by names
            if (value['user_from'].lower() == keyword.lower()):
                transactions_list[key] = value

        return transactions_list



