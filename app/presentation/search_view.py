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

    def get_items_list(self):
        return self.search_business_logic.items_list();

    def get_items_list_key(self,keyword):
        return self.search_business_logic.items_list_key(keyword);

    def index(self):
        return render_template('produtos.html', list_items=self.get_items_list(), title="Busca")

    def post(self):
        return render_template('produtos.html', list_items=self.get_items_list_key(request.form['search-key']), title="Busca")

SearchView.register(app)

