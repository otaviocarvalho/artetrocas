from app import app
from flask import render_template
from flask.ext.classy import FlaskView

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.business import Business

class LoginView(FlaskView):
    route_base = '/login'

    def __init__(self):
        self.business_logic = Business()

    def get_items_list(self):
        return self.business_logic.items_list();

    #@route("/login")
    def index(self):
        return render_template('produtos.html', list_items=self.get_items_list(), title="Login")

LoginView.register(app)
