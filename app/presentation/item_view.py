from app import app
from flask import render_template, request, session, flash
from flask.ext.classy import FlaskView

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.item_business import ItemBusiness

class ItemView(FlaskView):
    route_base = '/item'

    def __init__(self):
        self.item_business_logic = ItemBusiness()

    def index(self, item_id):
        return render_template('item.html', list_item=self.item_business_logic.get_item(int(item_id)), title="Item")

    def new(self):
        return render_template('item_insert.html', title="Novo Item")

    def post(self):
        self.item = {
                        'title': request.form['title'],
                        'author': request.form['author'],
                        'description': request.form['description'],
                        'school': request.form['school'],
                        'type': request.form['type'],
                        'quantity': request.form['quantity'],
                        'user_id': session['user_id']
                    }

        self.item_business_logic.insert_new_item(self.item)

        flash("Novo Item Inserido com Sucesso!")
        return render_template('item_insert.html', title="Novo Item")


ItemView.register(app)

