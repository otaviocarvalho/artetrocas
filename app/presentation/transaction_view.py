from app import app
from flask import render_template, request, session, redirect, flash
from flask.ext.classy import FlaskView

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.transaction_business import TransactionBusiness
from app.business.user_business import UserBusiness
from app.business.item_business import ItemBusiness

active_transaction = {72580: {'status': 'finished', 'list_items_to_qtd': [], 'list_items_from_qtd': [], 'list_items_from': [], 'user_to': None, 'user_from': None, 'list_items_to': []}}
active_transaction_key = active_transaction.keys()[0]

class TransactionView(FlaskView):
    route_base = '/transaction'

    def __init__(self):
        self.transaction_business_logic = TransactionBusiness()
        self.user_business_logic = UserBusiness()
        self.item_business_logic = ItemBusiness()

    def get_transactions_list(self):
        return self.transaction_business_logic.transactions_list()

    def get_transactions_list_key(self, user):
        return self.transaction_business_logic.transactions_list_key(user)

    def create_transaction(self):
        pass
        #return self.transaction_business_logic.create_transaction(session['user'])

    def get_user_items(self, user):
        return self.user_business_logic.get_user_items(user)

    def get_users_exchange_items(self, ids, qtds, user_id):
        return self.user_business_logic.get_users_exchange_items(ids, qtds, user_id)

    def set_transaction_item_from(self, transaction_id, form_id, form_qtd):
        return self.transaction_business_logic.set_transaction_item_from(transaction_id, form_id, form_qtd)

    def set_transaction_item_to(self, transaction_id, user_id, form_id, form_qtd):
        return self.transaction_business_logic.set_transaction_item_to(transaction_id, user_id, form_id, form_qtd)

    def get_transaction_by_id(self, transaction_id):
        return self.transaction_business_logic.get_transaction_by_id(transaction_id)

    def add_transaction(self, transaction):
        return self.transaction_business_logic.add_transaction(transaction)

    def get_user_by_id(self, user_id):
        users_list = self.user_business_logic.users_list()
        for k,v in users_list.iteritems():
            if str(k) == user_id:
                return v['name']


    #@app.route("/transaction/new/exchange/finish", methods=['GET', 'POST'])
    def new_transaction_finish(self):
        #transaction_view = TransactionView()

        #print 'active_transaction finish'
        print "/transaction/new/exchange/finish"
        print active_transaction

        # Demo set actual transation for test purposes
        transaction_view.add_transaction(active_transaction)

        # Insert items wanted into transaction
        user_id = request.form['user_id']
        user_name = transaction_view.get_user_by_id(user_id)

        form_ids = request.form['items_ids'].split(',')
        form_qtd = request.form['quantities'].split(',')
        if (len(form_ids) == len(form_qtd) and user_id != None):
            for i in range(0,len(form_ids)):
                #transaction_return = transaction_view.set_transaction_item_to(session['active_transaction'], user_id, form_ids[i], form_qtd[i])
                transaction_return = transaction_view.set_transaction_item_to(active_transaction_key, user_name, form_ids[i], form_qtd[i])
                if transaction_return == False:
                    transaction_error = True

        #print transaction_view.get_transaction_by_id(session['active_transaction'])
        #print transaction_view.get_transactions_list()
        print transaction_return
        print transaction_view.get_transaction_by_id(active_transaction_key)

        #if transaction_error == True:
            #flash("Houve um erro na Solicitacao de Troca, tente novamente mais tarde.")
        #else:
            #flash("Solicitacao de Troca criada com Sucesso!")
        #return redirect('/transaction')
        flash("Solicitacao de Troca criada com Sucesso!")

        #return render_template('transactions.html', list_transactions=transaction_view.get_transactions_list_key(), title="Transaction")
        return render_template('transactions.html', list_transactions=transaction_view.get_transactions_list(), title="Transacao")

    #@app.route("/transaction/new/exchange", methods=['GET', 'POST'])
    def new_transaction_users(self):
        #transaction_view = TransactionView()

        # Insert items into transaction
        form_ids = request.form['items_ids'].split(',')
        form_qtd = request.form['quantities'].split(',')
        if (len(form_ids) == len(form_qtd)):
            for i in range(0,len(form_ids)):
                #transaction_view.set_transaction_item_from(session['active_transaction'], form_ids[i], form_qtd[i])
                active_transaction[active_transaction_key]['user_from'] = "test"
                active_transaction[active_transaction_key]['list_items_from'].extend(form_ids[i])
                active_transaction[active_transaction_key]['list_items_from_qtd'].extend(form_qtd[i])

        transaction_view.add_transaction(active_transaction)
        print "/transaction/new/exchange"
        print active_transaction
        #print transaction_view.get_users_exchange_items(form_ids, form_qtd, session['user_id'])

        # Get list of users to trade
        #return render_template('transactions_create_exchange_users.html', list_users=transaction_view.get_users_exchange_items(form_ids, form_qtd, session['user_id']), title="New Transaction - Select User")

        #return render_template('transactions_create_exchange_users.html', list_users=transaction_view.get_users_exchange_items(form_ids, form_qtd, session['user_id']), title="New Transaction - Select User")

    #@app.route("/transaction/new")
    def new(self):
        # Create new transaction if there wasn't one active yet
        if not 'active_transaction' in session:
            create_transaction_id = self.create_transaction()
            print create_transaction_id
            session['active_transaction'] = create_transaction_id

        return render_template('transactions_create_user_items.html', list_items=self.get_user_items(session['user']), title="Nova Transacao - Itens do Usuario")

    #@app.route('/transaction')
    def index(self):
        #transaction_view = TransactionView()
        print "/transaction"
        print active_transaction

        session['user'] = 'test'
        session['user_id'] = 1
        #session['user'] = 'otavio'
        #session['user_id'] = 2

        #if 'active_transaction' in session:
            #self.active_transaction = session['active_transaction']

        return render_template('transactions.html', list_transactions=self.get_transactions_list_key(session['user']), title="Transacao")


TransactionView.register(app)
