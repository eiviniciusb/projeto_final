from flask import Flask

app = Flask(__name__)

# Carega as configurações a partir de confing.py
app.config.from_object('config')

from projeto_final import routes