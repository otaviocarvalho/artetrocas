from app import app
#from flask import Flask, render_template
from flask import render_template
from flask.ext.classy import FlaskView
#import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#print sys.path

#from app.business.business import Business
from app.business.search_business import SearchBusiness

#class Presentation(object):
class HomeView(FlaskView):
    route_base = '/'

    def __init__(self):
        #self.business_logic = Business()
        self.business_logic = SearchBusiness()

    def get_items_list(self):
        return self.business_logic.items_list();

    #@app.route("/")
    def index(self):
        #ui = Presentation()
        #return render_template('produtos.html', list_items=ui.get_items_list(), title="Index")
        return render_template('produtos.html', list_items=self.get_items_list(), title="Index")

HomeView.register(app)
