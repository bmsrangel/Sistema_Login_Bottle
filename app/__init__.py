# https://bootsnipp.com/
# Pode-se utilizar o venv para gerar a lista de requisitos de bibliotecas.
# Basta ir na pasta do projeto e usar o comando pip freeze > requirements.txt
from bottle import Bottle

app = Bottle()

from app.controllers import default
