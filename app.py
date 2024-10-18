from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('templates/index.html')

@app.route('/submit', methods=['POST'])
def add_dado():
    data = request.get_json()  
    nome = data.get('nome')
    email = data.get('email')
    senha = data.get('senha')
    confirmacao = data.get('confirmacao')

    novo_dado = bd(nome=nome, email=email, senha=senha, confirmacao=confirmacao)

    return f'Nome: {nome}, Email: {email}, Senha: {senha}'

if __name__ == '__main__':
    app.run(debug=True)
