from app import app
from flask.ext.classy import FlaskView, route
from flask import render_template, request, session, redirect, flash

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.transaction_business import TransactionBusiness
from app.business.user_business import UserBusiness
from app.business.item_business import ItemBusiness

class TransactionAcceptView(FlaskView):
    route_base = '/transaction/accept'

    def __init__(self):
        self.transaction_business_logic = TransactionBusiness()

    def index(self):
        # Lista as transacoes ativas aguardando aceitacao pelo usuario logado
        return render_template('transactions_accept.html', list_transactions=self.transaction_business_logic.transactions_waiting_list_user(session['user']), title="Solicitacoes")

    def post(self):
        # Processa a transacao
        if request.form['type'] == 'yes':
            self.transaction_business_logic.finish_transaction(request.form['transaction_id'])
            flash("Solicitacao #%s processada com Sucesso!" % request.form['transaction_id'])
        else:
            self.transaction_business_logic.cancel_transaction(request.form['transaction_id'])
            flash("Solicitacao #%s cancelada com Sucesso!" % request.form['transaction_id'])

        return render_template('transactions_accept.html', list_transactions=self.transaction_business_logic.transactions_waiting_list_user(session['user']), title="Solicitacoes")

TransactionAcceptView.register(app)
