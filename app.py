# https://bootsnipp.com/
# Pode-se utilizar o venv para gerar a lista de requisitos de bibliotecas.
# Basta ir na pasta do projeto e usar o comando pip freeze > requirements.txt
from bottle import *
import os


# static routes
@get('/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='static/css')


@get('/<filename:re:.*\.js>')
def javascript(filename):
    return static_file(filename, root='static/js')


@get('/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='static/img')


@get('/<filename:re:.*\.(eot|ttf|woff|svg)>')
def fonts(filename):
    return static_file(filename, root='static/fonts')


@route('/')  # @get('/')
def login():
    return template('login')


def check_login(username, password):
    d = {'marcos': 'python', 'joao': 'java', 'pedro': 'go'}
    return True if username in d.keys() and d[username] == password else False


# @route('/')
# def index():
#     return template('index')


@route('/', method='POST')  # @post('/')
def acao_login():
    username = request.forms.get('username')
    password = request.forms.get('password')
    return template('verificacao_login',
                    sucesso=check_login(username, password),
                    nome=username)


@error(404)
def error404(error):
    return template('page404')


if __name__ == '__main__':
    if os.environ.get('APP_LOCATION') == 'heroku':
        run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
    else:
        run(host='localhost', port=8080, reloader=True)
