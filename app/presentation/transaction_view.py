from app import app
from flask import render_template, request, session, redirect, flash
from flask.ext.classy import FlaskView, route

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.transaction_business import TransactionBusiness
from app.business.user_business import UserBusiness
from app.business.item_business import ItemBusiness

class TransactionView(FlaskView):
    route_base = '/transaction'

    def __init__(self):
        self.transaction_business_logic = TransactionBusiness()

    def index(self):
        return render_template('transactions.html', list_transactions=self.transaction_business_logic.transactions_list_key(session['user']), title="Transacao")


TransactionView.register(app)
