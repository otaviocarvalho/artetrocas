from flask import Flask
import locale

locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")

app = Flask("app")

from presentation import presentation

