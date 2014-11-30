from app import app
from flask import render_template, request, session, flash
from flask.ext.classy import FlaskView

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.transaction_business import TransactionBusiness
from app.business.user_business import UserBusiness
from app.business.item_business import ItemBusiness

class TransactionCreateView(FlaskView):
    route_base = '/transaction/create'

    def __init__(self):
        self.transaction_business_logic = TransactionBusiness()
        self.user_business_logic = UserBusiness()
        self.item_business_logic = ItemBusiness()

    def get_user_by_id(self, user_id):
        users_list = self.user_business_logic.users_list()
        for k,v in users_list.iteritems():
            if str(k) == user_id:
                return v['name']

    def post(self):
        # Recebe os itens pelos quais o usuario deseja trocar os seus
        user_id = int(request.form['user_id'])
        form_ids = request.form['items_ids'].split(',')
        form_ids = [x.encode('utf-8') for x in form_ids]
        form_qtd = request.form['quantities'].split(',')
        form_qtd = [x.encode('utf-8') for x in form_qtd]

        # Insere os itens na transacao
        if (len(form_ids) == len(form_qtd) and user_id != None):
            for i in range(0,len(form_ids)):
                transaction_return = self.transaction_business_logic.set_transaction_item_to(session['active_transaction_key'], user_id, form_ids[i], form_qtd[i])
                if transaction_return == False:
                    transaction_error = True

        # Finaliza edicao da transacao pelo proponente
        session.pop('active_transaction', None)
        session.pop('active_transaction_key', None)

        # Imprime a mensagem ao concluir a transacao
        flash("Solicitacao de Troca criada com Sucesso!")
        return render_template('transactions.html', list_transactions=self.transaction_business_logic.transactions_list(), title="Transacao")

TransactionCreateView.register(app)
