from app import app
from flask import render_template
from flask.ext.classy import FlaskView

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from app.business.search_business import SearchBusiness
from app.business.user_business import UserBusiness

class LoginView(FlaskView):
    route_base = '/login'

    def __init__(self):
        self.search_business_logic = SearchBusiness()

    def get_items_list(self):
        return self.search_business_logic.items_list();

    def index(self):
        return render_template('produtos.html', list_items=self.get_items_list(), title="Login")

LoginView.register(app)
