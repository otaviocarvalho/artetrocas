from app import app
from flask import render_template, request, session, flash, redirect
from flask.ext.classy import FlaskView, route

import json
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
        session['user'] = 'test'
        session['user_id'] = 1

        # Cria novo item vazio
        self.item = self.item_business_logic.create_item(session['user_id'])
        self.list_item = {}

        # Busca o id no json
        for key in self.item.keys():
            self.list_item['id'] = key

        # Transforma para um novo json
        for key in self.item[self.list_item['id']]:
            self.list_item[key] = self.item[self.list_item['id']][key]

        return render_template('item_insert.html', list_item=self.list_item, title="Criacao de Novo Item")

    def index(self, item_id):
        return render_template('item.html', list_item=self.get_item_by_key(int(item_id)), title="Descricao do Item")

    def post(self):
        item = {}

        # Processa o request
        item['id'] = int(str(request.form['id']))
        item['school'] = str(request.form['school'])
        item['quantity'] = int(str(request.form['quantity']))
        item['title'] = str(request.form['title'])
        item['user_id'] = int(str(request.form['user_id']))

        # Insere o novo item no db
        item_json = { item['id']: {'title': item['title'], 'school': item['school'], 'quantity': item['quantity'], 'user_id': item['user_id']} }
        self.item_business_logic.insert_item(item_json)

        flash("Item criado com Sucesso!")
        return redirect('/item/new')

ItemView.register(app)
