from app import app
from flask import render_template, request
from flask.ext.classy import FlaskView

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.search_business import SearchBusiness

class SearchView(FlaskView):
    route_base = '/search'

    def __init__(self):
        self.search_business_logic = SearchBusiness()

    def index(self):
        return render_template('produtos.html', list_items=self.search_business_logic.items_list(), title="Busca")

    def post(self):
        return render_template('produtos.html', list_items=self.search_business_logic.items_list_key(request.form['search-key']), title="Busca")

SearchView.register(app)

