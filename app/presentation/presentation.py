from app import app
from flask import Flask, render_template
import datetime

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
#print sys.path

from app.business.business import BusinessLogic

### UI interaction class ###
class Presentation(object):
    def __init__(self):
        self.business_logic = BusinessLogic()

    @app.route("/")
    def main():
        ui = Presentation()
        ui.get_product_list()

        return render_template('produtos.html', my_string="Wheeeee!",
            my_list=ui.get_product_list(), title="Index", current_time=datetime.datetime.now())

    @app.route("/home")
    def home():
        print "home"
        return render_template('template.html', my_string="Foo",
            my_list=[6,7,8,9,10,11], title="Home", current_time=datetime.datetime.now())

    @app.route("/about")
    def about():
        return render_template('template.html', my_string="Bar",
            my_list=[12,13,14,15,16,17], title="About", current_time=datetime.datetime.now())

    @app.route("/contact")
    def contact():
        return render_template('template.html', my_string="FooBar"
            , my_list=[18,19,20,21,22,23], title="Contact Us", current_time=datetime.datetime.now())

    def get_product_list(self):
        #print('PRODUCT LIST:')
        #for product in self.business_logic.product_list():
            #print(product)
            #yield product
        #print('')
        return self.business_logic.product_list();

    def get_product_information(self, product):
        product_info = self.business_logic.product_information(product)
        if product_info:
            print('PRODUCT INFORMATION:')
            print('Name: {0}, Price: {1:.2f}, Quantity: {2:}'.format(
                product.title(), product_info.get('price', 0),
                product_info.get('quantity', 0)))
        else:
            print('That product "{0}" does not exist in the records'.format(
                product))



