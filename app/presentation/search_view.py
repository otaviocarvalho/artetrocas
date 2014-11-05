from app import app
from flask import render_template, request

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.search_business import SearchBusiness

class SearchView(object):
    def __init__(self):
        self.search_business_logic = SearchBusiness()

    def get_items_list(self):
        return self.search_business_logic.items_list();

    def get_items_list_key(self,keyword):
        return self.search_business_logic.items_list_key(keyword);


    @app.route("/search", methods=['GET', 'POST'])
    def search():
        search_view = SearchView()

        if request.method == 'GET':
            return render_template('produtos.html', list_items=search_view.get_items_list(), title="Search")
        elif request.method == 'POST':
            #print request.form
            return render_template('produtos.html', list_items=search_view.get_items_list_key(request.form['search-key']), title="Search")

    @app.route("/search/<keyword>")
    def search_key(keyword=None):
        search_view = SearchView()
        #return render_template('produtos.html', list_items=search_view.get_items_list(), title="Search")
        return render_template('produtos.html', list_items=search_view.get_items_list_key(keyword), title=keyword)