from app.data.transaction_data import TransactionData

class TransactionBusiness(object):
    #item_data = ItemData()
    #user_data = UserData()
    transaction_data = TransactionData()

    def transactions_list(self):
        return self.transaction_data.get_transactions()

    def transactions_list_key(self, keyword):
        return self.transaction_data.get_transaction_key(keyword)
