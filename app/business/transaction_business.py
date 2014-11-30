from app.data.transaction_data import TransactionData
from app.data.item_data import ItemData
from app.data.user_data import UserData

class TransactionBusiness(object):
    item_data = ItemData()
    user_data = UserData()
    transaction_data = TransactionData()

    def transactions_list(self):
        return self.transaction_data.get_transactions()

    def transactions_list_key(self, keyword):
        return self.transaction_data.get_transaction_key(keyword)

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

    def commit_transaction(self, transaction_id):
        return self.transaction_data.commit_transaction(transaction_id)
