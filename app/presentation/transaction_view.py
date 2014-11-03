from app import app
from flask import render_template, request, session

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.transaction_business import TransactionBusiness
from app.business.user_business import UserBusiness
from app.business.item_business import ItemBusiness

class TransactionView(object):
    def __init__(self):
        self.transaction_business_logic = TransactionBusiness()
        self.user_business_logic = UserBusiness()
        self.item_business_logic = ItemBusiness()
        #session['user'] = 'otavio'
        session['user'] = 'test'
        session['user_type'] = 'user'

    def get_transactions_list(self):
        return self.transaction_business_logic.transactions_list();

    def get_transactions_list_key(self):
        return self.transaction_business_logic.transactions_list_key(session['user']);

    @app.route("/transaction", methods=['GET', 'POST'])
    def transaction():
        transaction_view = TransactionView()

        # Create empty transaction
        # Get user items
        # Select items to exchange
        # Select quantities to exchange
        # List users to exchange products
        # Select user to exchange
        # List user items to exchange
        # Select user items quantities
        # Save transaction

        #return render_template('transactions.html', list_transactions=transaction_view.get_transactions_list(), title="Transaction")
        return render_template('transactions.html', list_transactions=transaction_view.get_transactions_list_key(), title="Transaction")
