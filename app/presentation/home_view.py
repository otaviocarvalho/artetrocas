from app import app
from flask import render_template, session
from flask.ext.classy import FlaskView

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.search_business import SearchBusiness

# Parametros de sessao para simular o login
user = 'test'
user_id = 1

class HomeView(FlaskView):
    route_base = '/'

    def __init__(self):
        #self.business_logic = Business()
        self.search_business_logic = SearchBusiness()

    def index(self):
        # Cria uma sessao para simular o login
        session['user'] = user
        session['user_id'] = user_id

        return render_template('produtos.html', list_items=self.search_business_logic.items_list(), title="Index")

HomeView.register(app)
