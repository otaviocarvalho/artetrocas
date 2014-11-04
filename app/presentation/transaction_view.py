from app import app
from flask import render_template, request, session, redirect, flash

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
        #session['user_id'] = 2
        session['user'] = 'test'
        session['user_id'] = 1
        session['user_type'] = 'user'
        session['active_transaction'] = None

    def get_transactions_list(self):
        return self.transaction_business_logic.transactions_list()

    def get_transactions_list_key(self):
        return self.transaction_business_logic.transactions_list_key(session['user'])

    def create_transaction(self):
        return self.transaction_business_logic.create_transaction(session['user'])

    def get_user_items(self):
        return self.user_business_logic.get_user_items(session['user_id'])

    def get_users_exchange_items(self, ids, qtds):
        return self.user_business_logic.get_users_exchange_items(ids, qtds)

    def set_transaction_item(self, transaction_id, form_id, form_qtd):
        return self.transaction_business_logic.set_transaction_item(transaction_id, form_id, form_qtd)

    @app.route("/transaction/new/exchange/finish", methods=['GET', 'POST'])
    def new_transaction_finish():
        flash("Solicitacao de Troca criada com Sucesso!")
        return redirect('/transaction')

    @app.route("/transaction/new/exchange", methods=['GET', 'POST'])
    def new_transaction_users():
        transaction_view = TransactionView()
        # Insert items into transaction
        form_ids = request.form['items_ids'].split(',')
        form_qtd = request.form['quantities'].split(',')
        if (len(form_ids) == len(form_qtd)):
            for i in range(0,len(form_ids)):
                transaction_view.set_transaction_item(session['active_transaction'], form_ids[i], form_qtd[i])

        # Get list of users to trade
        return render_template('transactions_create_exchange_users.html', list_users=transaction_view.get_users_exchange_items(form_ids, form_qtd), title="New Transaction - Select User")

    @app.route("/transaction/new", methods=['GET', 'POST'])
    def new_transaction():
        transaction_view = TransactionView()

        # Create new transaction if there wasn't one active yet
        if session['active_transaction'] == None:
            create_transaction_id = transaction_view.create_transaction()
        return render_template('transactions_create_user_items.html', list_items=transaction_view.get_user_items(), title="New Transaction - User Items")

    @app.route("/transaction", methods=['GET', 'POST'])
    def transaction():
        transaction_view = TransactionView()

        return render_template('transactions.html', list_transactions=transaction_view.get_transactions_list_key(), title="Transaction")
