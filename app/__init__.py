# https://bootsnipp.com/
# Pode-se utilizar o venv para gerar a lista de requisitos de bibliotecas.
# Basta ir na pasta do projeto e usar o comando pip freeze > requirements.txt
from bottle import Bottle
from bottle import TEMPLATE_PATH
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
engine = create_engine('sqlite:///database.db', echo=True)
# engine = create_engine('sqlite:///:memory:', echo=True)

app = Bottle()
TEMPLATE_PATH.insert(0, 'app/views/')
plugin = sqlalchemy.Plugin(
    engine,
    Base.metadata,
    keyword='db',
    create=True,
    commit=True,
    use_kwargs=False
)

app.install(plugin)


from app.controllers import default
from app.models import tables
