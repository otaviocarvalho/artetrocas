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
        return self.transaction_data.create_transaction(user_id)

    def set_transaction_item(self, transaction_id, item_id, item_qtd):
        # Verify items before insert
        return self.transaction_data.set_transaction_item(transaction_id, item_id, item_qtd)

