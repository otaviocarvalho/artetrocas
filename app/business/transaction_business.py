from app.data.transaction_data import TransactionData
from app.data.item_data import ItemData
from app.data.user_data import UserData

import copy

class TransactionBusiness(object):
    item_data = ItemData()
    user_data = UserData()
    transaction_data = TransactionData()

    def transactions_list(self):
        return self.transaction_data.get_transactions()

    def transactions_list_key(self, keyword):
        return self.transaction_data.get_transaction_key(keyword)

    def transactions_waiting_list_user(self, user_id):
        return self.transaction_data.get_transaction_user_status(user_id, 'open')

    def create_transaction(self, user_id):
        user = self.user_data.get_user_id(int(user_id))
        return self.transaction_data.create_transaction(user[user.keys()[0]]['name'])

    # Atualiza os itens que serao enviados na troca
    def set_transaction_item_from(self, transaction_id, item_id, item_qtd):
        return self.transaction_data.set_transaction_item_from(transaction_id, item_id, item_qtd)

    # Atualiza os itens que serao recebidos na troca
    def set_transaction_item_to(self, transaction_id, user_id, item_id, item_qtd):
        user = self.user_data.get_user_id(int(user_id))
        return self.transaction_data.set_transaction_item_to(transaction_id, user[user.keys()[0]]['name'], item_id, item_qtd)

    def get_transaction_by_id(self, transaction_id):
        return self.transaction_data.get_transaction_by_id(transaction_id)

    def add_transaction(self, transaction):
        return self.transaction_data.add_transaction(transaction)

    def set_status_transaction(self, transaction_id, status):
        return self.transaction_data.commit_transaction(transaction_id, status)

    def cancel_transaction(self, transaction_id):
        return self.transaction_data.cancel_transaction(transaction_id)

    def finish_transaction(self, transaction_id):
        # Busca dados da transacao
        transaction = self.get_transaction_by_id(transaction_id)
        print transaction

        # Decrementa itens do solicitante e incrementa no solicitado
        for index in range(len(transaction['list_items_from'])):
            # Decrementa solicitante
            item_id = int(transaction['list_items_to'][index])
            item = self.item_data.get_item(item_id)
            quantity = item['quantity'] - int(transaction['list_items_to_qtd'][index])
            self.item_data.set_item_quantity(item_id, quantity)
            # Adiciona ao solicitado
            item_insert = copy.deepcopy(item)
            item_insert['user_id'] = self.user_data.get_user_key(transaction['user_to']).keys()[0]
            item_insert['quantity'] = int(transaction['list_items_to_qtd'][index])
            self.item_data.insert_new_item(item_insert)

        # Decrementa itens do solicitado e incrementa no solicitante
        for index in range(len(transaction['list_items_to'])):
            # Decrementa solicitado
            item_id = int(transaction['list_items_from'][index])
            item = self.item_data.get_item(item_id)
            quantity = item['quantity'] - int(transaction['list_items_from_qtd'][index])
            self.item_data.set_item_quantity(item_id, quantity)
            # Adiciona ao solicitante
            item_insert = copy.deepcopy(item)
            item_insert['user_id'] = self.user_data.get_user_key(transaction['user_from']).keys()[0]
            item_insert['quantity'] = int(transaction['list_items_from_qtd'][index])
            self.item_data.insert_new_item(item_insert)


        return self.transaction_data.finish_transaction(transaction_id)

