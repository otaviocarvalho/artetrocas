from app import app
from flask import Flask, render_template
import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#print sys.path

from app.business.business import Business

class Presentation(object):
    def __init__(self):
        self.business_logic = Business()

    def get_items_list(self):
        return self.business_logic.items_list();

    @app.route("/")
    def main():
        ui = Presentation()
        return render_template('produtos.html', list_items=ui.get_items_list(), title="Index")
