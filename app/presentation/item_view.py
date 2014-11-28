from app import app
from flask import render_template, request, session
from flask.ext.classy import FlaskView

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.item_business import ItemBusiness

class ItemView(FlaskView):
    route_base = '/item'

    def __init__(self):
        self.item_business_logic = ItemBusiness()

    def get_item_by_key(self, item_id):
        return self.item_business_logic.get_item(item_id);

    def new(self):
        print "here create item"
        item = self.item_business_logic.create_item(session['user_id'])

    def index(self, item_id):
        return render_template('item.html', item_id=item_id, list_item=self.get_item_by_key(int(item_id)), title="Descricao do Item")

    #def post(self):
        #return render_template('produtos.html', list_items=self.get_items_list_key(request.form['search-key']), title="Search")

    #@app.route('/search/<keyword>')
    #def search_key(self, keyword):
        #return render_template('produtos.html', list_items=self.get_items_list_key(keyword), title=keyword)

ItemView.register(app)

