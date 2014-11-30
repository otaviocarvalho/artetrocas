from app import app
from flask import render_template, request, session, redirect, flash
from flask.ext.classy import FlaskView, route

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.transaction_business import TransactionBusiness
from app.business.user_business import UserBusiness
from app.business.item_business import ItemBusiness

# Parametros de sessao para simular o login
#active_transaction = {72580: {'status': 'finished', 'list_items_to_qtd': [], 'list_items_from_qtd': [], 'list_items_from': [], 'user_to': None, 'user_from': None, 'list_items_to': []}}
#active_transaction_key = active_transaction.keys()[0]
user = 'test'
user_id = 1

class TransactionView(FlaskView):
    route_base = '/transaction'

    def __init__(self):
        self.transaction_business_logic = TransactionBusiness()
        self.user_business_logic = UserBusiness()
        self.item_business_logic = ItemBusiness()

    def index(self):
        # Cria uma sessao para simular o login
        #session['active_transaction_key'] = active_transaction_key
        #session['active_transaction'] = active_transaction
        session['user'] = user
        session['user_id'] = user_id

        return render_template('transactions.html', list_transactions=self.transaction_business_logic.transactions_list_key(session['user']), title="Transacao")


TransactionView.register(app)
