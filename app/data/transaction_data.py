import random

transactions = {
    '12345': {'user_from': 'test', 'user_to': 'otavio', 'status': 'finished', 'list_items_from': ['0', '1'], 'list_items_from_qtd': ['1', '1'],
                                                                                'list_items_to': ['2', '3'], 'list_items_to_qtd': ['1', '1'] },

    '12346': {'user_from': 'test', 'user_to': 'otavio', 'status': 'open', 'list_items_from': ['0', '1'], 'list_items_from_qtd': ['1', '1'],
                                                                                'list_items_to': ['2', '3'], 'list_items_to_qtd': ['1', '1'] },

    '12347': {'user_from': 'test', 'user_to': 'otavio', 'status': 'empty', 'list_items_from': ['0', '1'], 'list_items_from_qtd': ['1', '1'],
                                                                                'list_items_to': ['2', '3'], 'list_items_to_qtd': ['1', '1'] },

    '12348': {'user_from': 'otavio', 'user_to': 'test', 'status': 'open', 'list_items_from': ['2'], 'list_items_from_qtd': ['1'],
                                                                                'list_items_to': ['1'], 'list_items_to_qtd': ['1'] },
}

class TransactionData(object):
    class __TransactionData:
        def __init__(self):
            self.transactions = transactions

        def get_transactions(self):
            return self.transactions

        def get_transaction_by_id(self, transaction_id):
            return self.transactions[transaction_id]

        def get_transaction_key(self, keyword):
            transactions_list = {}
            for key,value in self.transactions.iteritems():
                # Mostra apenas as transacoes ativas
                if value['status'] != 'empty':
                    # Procura por nomes
                    if (value['user_from'].lower() == keyword.lower()):
                        transactions_list[key] = value

            return transactions_list

        def get_transaction_user_status(self, user, status):
            transactions_list = {}
            for key,value in self.transactions.iteritems():
                # Mostra apenas as transacoes aguardando
                if value['status'] == status:
                    # Procura por nomes
                    if (value['user_to'].lower() == user.lower()):
                        transactions_list[key] = value

            return transactions_list

        def create_transaction(self, user_from):
            # Procura uma chave que ainda nao esteja no dicionario
            new_key = random.randrange(10000, 99999)
            while new_key in self.transactions.keys():
                new_key = random.randrange(10000, 99999)

            new_transaction = { 'user_from': user_from, 'user_to': None, 'status': 'empty', 'list_items_from': [], 'list_items_from_qtd': [],
                                                                                            'list_items_to': [], 'list_items_to_qtd': [] }
            self.transactions[new_key] = new_transaction
            return { new_key: new_transaction }

        def set_transaction_item_from(self, transaction_id, item_id, item_qtd):
            if transaction_id in self.transactions.keys():
                self.transactions[transaction_id]['list_items_from'].extend(item_id)
                self.transactions[transaction_id]['list_items_from_qtd'].extend(item_qtd)
                return True
            else:
                return False

        def set_transaction_item_to(self, transaction_id, user, item_id, item_qtd):
            if transaction_id in self.transactions.keys():
                self.transactions[transaction_id]['user_to'] = user
                self.transactions[transaction_id]['list_items_to'].extend(item_id)
                self.transactions[transaction_id]['list_items_to_qtd'].extend(item_qtd)
                return True
            else:
                return False

        def add_transaction(self, transaction):
            if not transaction.keys()[0] in self.transactions:
                for key,value in transaction.iteritems():
                    self.transactions[key] = value

        def set_status_transaction(self, transaction_id, status):
            if transaction_id in self.transactions.keys():
                self.transactions[transaction_id]['status'] = status

        def finish_transaction(self, transaction_id):
            # Muda o status da transacao
            self.transactions[transaction_id]['status'] = 'finished'

        def cancel_transaction(self, transaction_id):
            if transaction_id in self.transactions.keys():
                del self.transactions[transaction_id]

    instance = None
    def __new__(cls):
        if not TransactionData.instance:
            TransactionData.instance = TransactionData.__TransactionData()
        return TransactionData.instance


