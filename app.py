from flask import Flask, render_template, request
from werkzeug.utils import quote

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return "bem vindo a minha aplicação Flask!"

# Rota com renderização de template (corrigida)
@app.route('/hello/<string:name>')
def hello(name):
    return render_template('./hello.html', name=name)

# Rota para receber dados de um formulário HTML
@app.route('/submit', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
    return f'Olá, {name}! Seu formulário foi enviado com sucesso!'

if __name__ == "__main__":
    app.run(debug=True)




