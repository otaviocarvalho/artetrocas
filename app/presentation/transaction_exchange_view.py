from app import app
from flask import render_template, request, session
from flask.ext.classy import FlaskView

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.transaction_business import TransactionBusiness
from app.business.user_business import UserBusiness
from app.business.item_business import ItemBusiness

class TransactionExchangeView(FlaskView):
    route_base = '/transaction/exchange'

    def __init__(self):
        self.transaction_business_logic = TransactionBusiness()
        self.user_business_logic = UserBusiness()
        self.item_business_logic = ItemBusiness()

    def post(self):
        # Recebe os itens a serem trocados
        form_ids = request.form['items_ids'].split(',')
        form_ids = [x.encode('utf-8') for x in form_ids]
        form_qtd = request.form['quantities'].split(',')
        form_qtd = [x.encode('utf-8') for x in form_qtd]

        # Insere os itens escolhidos para troca, na etapa anterior, na transacao
        if (len(form_ids) == len(form_qtd)):
            for i in range(0,len(form_ids)):
                self.transaction_business_logic.set_transaction_item_from(session['active_transaction_key'], form_ids[i], form_qtd[i])

        return render_template('transactions_create_exchange_users.html', list_users=self.user_business_logic.get_users_exchange_items(form_ids, form_qtd, session['user_id']), title="New Transaction - Select User")

TransactionExchangeView.register(app)
