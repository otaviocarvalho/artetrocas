from app import app
from flask import render_template

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.business import Business

class LoginView(object):
    def __init__(self):
        self.business_logic = Business()

    def get_items_list(self):
        return self.business_logic.items_list();

    @app.route("/login")
    def login():
        login_view = LoginView()
        return render_template('produtos.html', list_items=login_view.get_items_list(), title="Login")
