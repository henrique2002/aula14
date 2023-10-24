from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/usuario/<nome>')
def usuario(nome):
  return render_template('usuario.html', nome=nome)

app.run(debug=True)