import random

list_transactions = {
    '12345': {
                'user_from': 'test',
                'user_to': 'otavio',
                'status': 'finished',
                'list_items_from': ['0', '1'],
                'list_items_from_qtd': ['1', '1'],
                'list_items_to': ['2', '3'],
                'list_items_to_qtd': ['1', '1']
            },
    '12346': {
                'user_from': 'test',
                'user_to': 'otavio',
                'status': 'open',
                'list_items_from': ['0', '1'],
                'list_items_from_qtd': ['1', '1'],
                'list_items_to': ['2', '3'],
                'list_items_to_qtd': ['1', '1']
            },
    '12347': {
            'user_from': 'test',
            'user_to': 'otavio',
            'status': 'empty',
            'list_items_from': ['0', '1'],
            'list_items_from_qtd': ['1', '1'],
            'list_items_to': ['2', '3'],
            'list_items_to_qtd': ['1', '1']
            },
    '12348': {
            'user_from': 'otavio',
            'user_to': 'test',
            'status': 'open',
            'list_items_from': ['2'],
            'list_items_from_qtd': ['2'],
            'list_items_to': ['1'],
            'list_items_to_qtd': ['1']
            },
}

class TransactionData(object):
    class __TransactionData:
        def __init__(self):
            self.list_transactions = list_transactions

        def get_transactions(self):
            #return self.list_transactions
            list_aux = []
            for transaction_key in self.list_transactions.keys():
                list_aux.append(self.convert_dict_to_transaction(self.list_transactions[transaction_key], transaction_key))

            return list_aux

        def get_transaction_by_id(self, transaction_id):
            #return self.list_transactions[transaction_id]
            transaction = self.convert_dict_to_transaction(self.list_transactions[transaction_id], transaction_id)
            return transaction

        def get_transaction_key(self, keyword):
            #transactions_list = {}
            #for key,value in self.list_transactions.iteritems():
                # Mostra apenas as transacoes ativas
                #if value['status'] != 'empty':
                    # Procura por nomes
                    #if (value['user_from'].lower() == keyword.lower()):
                        #transactions_list[key] = value
            #return transactions_list
            transactions_list = self.get_transactions()
            transactions_list_aux = []
            for transaction in transactions_list:
                if transaction.status.lower() != 'empty':
                    # Procurar por nomes
                    if transaction.user_from.lower() == keyword.lower():
                        transactions_list_aux.append(transaction)

            return transactions_list_aux

        def get_transaction_user_status(self, user, status):
            #transactions_list = {}
            #for key,value in self.list_transactions.iteritems():
                # Mostra apenas as transacoes aguardando
                #if value['status'] == status:
                    # Procura por nomes
                    #if (value['user_to'].lower() == user.lower()):
                        #transactions_list[key] = value
            #return transactions_list
            transactions_list = self.get_transactions()
            transactions_list_aux = []
            for transaction in transactions_list:
                if transaction.status.lower() == status.lower():
                    # Procurar por nomes
                    if transaction.user_to.lower() == user.lower():
                        transactions_list_aux.append(transaction)

            return transactions_list_aux

        def create_transaction(self, user_from):
            # Procura uma chave que ainda nao esteja no dicionario
            new_key = random.randrange(10000, 99999)
            while new_key in self.list_transactions.keys():
                new_key = random.randrange(10000, 99999)

            new_transaction = { 'user_from': user_from, 'user_to': None, 'status': 'empty', 'list_items_from': [], 'list_items_from_qtd': [],
                                                                                            'list_items_to': [], 'list_items_to_qtd': [] }
            self.list_transactions[new_key] = new_transaction

            return self.convert_dict_to_transaction( { new_key: new_transaction } )
            #return { new_key: new_transaction }

        def set_transaction_item_from(self, transaction_id, item_id, item_qtd):
            if transaction_id in self.list_transactions.keys():
                self.list_transactions[transaction_id]['list_items_from'].extend(item_id)
                self.list_transactions[transaction_id]['list_items_from_qtd'].extend(item_qtd)
                return True
            else:
                return False

        def set_transaction_item_to(self, transaction_id, user, item_id, item_qtd):
            if transaction_id in self.list_transactions.keys():
                self.list_transactions[transaction_id]['user_to'] = user
                self.list_transactions[transaction_id]['list_items_to'].extend(item_id)
                self.list_transactions[transaction_id]['list_items_to_qtd'].extend(item_qtd)
                return True
            else:
                return False

        def set_status_transaction(self, transaction_id, status):
            if transaction_id in self.list_transactions.keys():
                self.list_transactions[transaction_id]['status'] = status
            return True

        def add_transaction(self, transaction):
            if not transaction.keys()[0] in self.list_transactions:
                for key,value in transaction.iteritems():
                    self.list_transactions[key] = value
                return True
            else:
                return False

        def finish_transaction(self, transaction_id):
            # Muda o status da transacao
            self.list_transactions[transaction_id]['status'] = 'finished'
            return True

        def cancel_transaction(self, transaction_id):
            if transaction_id in self.list_transactions.keys():
                del self.list_transactions[transaction_id]
            return True

        def generate_key(self):
            # Procura uma chave que ainda nao esteja no dicionario
            new_key = random.randrange(10000, 99999)
            while new_key in self.list_transactions.keys():
                new_key = random.randrange(10000, 99999)

            return new_key

        def convert_transaction_to_dict(self, transaction):
            # Cria um novo dicionario
            new_dict = {
                            'user_from': transaction.user_from,
                            'user_to': transaction.user_to,
                            'status': transaction.status,
                            'list_items_from': transaction.list_items_from,
                            'list_items_from_qtd': transaction.list_items_from_qtd,
                            'list_items_to': transaction.list_items_to,
                            'list_items_to_qtd': transaction.list_items_to_qtd,
                       }

            return { transaction.key : new_dict }

        def convert_dict_to_transaction(self, transaction_dict, transaction_key=None):
            if transaction_key is None:
                transaction = Transaction()
                transaction_key = transaction_dict.keys()[0]
                transaction_dict = transaction_dict[transaction_key]
            else:
                transaction = Transaction(transaction_key)

            transaction.key = transaction_key
            transaction.user_from = transaction_dict['user_from']
            transaction.user_to = transaction_dict['user_to']
            transaction.status = transaction_dict['status']
            transaction.list_items_from = transaction_dict['list_items_from']
            transaction.list_items_from_qtd = transaction_dict['list_items_from_qtd']
            transaction.list_items_to = transaction_dict['list_items_to']
            transaction.list_items_to_qtd = transaction_dict['list_items_to_qtd']

            return transaction

    instance = None
    def __new__(cls):
        if not TransactionData.instance:
            TransactionData.instance = TransactionData.__TransactionData()
        return TransactionData.instance

class Transaction(object):
    def __init__(self, key=-1, user_from="", user_to="", status="", list_items_from=[], list_items_from_qtd=[], list_items_to=[], list_items_to_qtd=[]):
        self.key = key
        self.user_from = user_from
        self.user_to = user_to
        self.list_items_from = list_items_from
        self.list_items_from_qtd = list_items_from_qtd
        self.list_items_to = list_items_to
        self.list_items_to_qtd = list_items_to_qtd
