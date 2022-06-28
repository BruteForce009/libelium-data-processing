from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from appdir.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)


def split_func(strn):
    t = f'{strn}'
    return t.split()


app.jinja_env.globals.update(split_func=split_func)

from appdir import routes