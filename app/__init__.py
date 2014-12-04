from flask import Flask
import locale
import os

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

app = Flask("app")

app.secret_key = os.urandom(24)

from app.presentation import home_view
from app.presentation import search_view
from app.presentation import item_view

from app.presentation import transaction_view
from app.presentation import transaction_select_view
from app.presentation import transaction_exchange_view
from app.presentation import transaction_create_view
from app.presentation import transaction_accept_view
