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
        # Cria um novo item vazio
        self.item = self.item_business_logic.create_item(session['user_id'])
        self.item.title = request.form['title'].encode('utf-8')
        self.item.author = request.form['author'].encode('utf-8')
        self.item.description = request.form['description'].encode('utf-8')
        self.item.school = request.form['school'].encode('utf-8')
        self.item.type = request.form['type'].encode('utf-8')
        self.item.quantity = int(request.form['quantity'].encode('utf-8'))
        self.item.user_id = session['user_id']

        #print self.item_business_logic.convert_item_to_dict(self.item)
        ## Insere novo item no banco de dados
        insert_result = self.item_business_logic.insert_new_item(self.item)

        if insert_result is True:
            flash("Novo Item Inserido com Sucesso!")
        else:
            flash("Nao foi possivel inserir o item, tente novamente mais tarde.")
        return render_template('item_insert.html', title="Novo Item")


ItemView.register(app)

