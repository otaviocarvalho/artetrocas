from app import app
from flask.ext.classy import FlaskView, route
from flask import render_template, request, session, redirect, flash

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.transaction_business import TransactionBusiness
from app.business.user_business import UserBusiness
from app.business.item_business import ItemBusiness

class TransactionSelectView(FlaskView):
    route_base = '/transaction/select'

    def __init__(self):
        self.transaction_business_logic = TransactionBusiness()
        self.user_business_logic = UserBusiness()

    def index(self):
        # Cria uma nova transacao se nao existir uma ativa ainda
        if not 'active_transaction' in session.keys():
            transaction = self.transaction_business_logic.create_transaction(session['user_id'])
            #session['active_transaction'] = transaction.key
            session['active_transaction_key'] = transaction.key
            #create_transaction_id = self.transaction_business_logic.create_transaction(session['user_id'])
            #session['active_transaction'] = create_transaction_id
            #session['active_transaction_key'] = create_transaction_id.keys()[0]

        return render_template('transactions_create_user_items.html', list_items=self.user_business_logic.get_user_items(session['user_id']), title="Nova Transacao - Itens do Usuario")

TransactionSelectView.register(app)
