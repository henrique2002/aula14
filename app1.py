from flask import Flask
# cria a aplicação Flask
app = Flask(__name__)

# endereço raiz do site
@app.route('/')
def index():
    return "<h1>Olá UNIFEI!</h1>"

# endereço do usuário do site
@app.route('/usuario/<nome>')
def usuario(nome):
	return '<h1>Olá, {0}!</h1>'.format(nome)

# executando o servidor de página 
app.run(debug=True)