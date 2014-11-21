from flask import Flask, session
import locale
import os

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

app = Flask("app")

app.secret_key = os.urandom(24)

from app.presentation import home_view
from app.presentation import login_view
from app.presentation import user_view
from app.presentation import subscribe_view
from app.presentation import complaint_view
from app.presentation import search_view
from app.presentation import item_view
from app.presentation import transaction_view
from app.presentation import profile_view
