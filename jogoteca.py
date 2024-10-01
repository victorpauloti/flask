from flask import Flask, render_template, request, redirect, session, flash

class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console

# fator global
jogo1 = Jogo('Super Mario Bros', 'Aventura', 'SNES')
jogo2 = Jogo('Zelda Breath of the Wild', 'Aventura', 'Switch')
jogo3 = Jogo('Pokemon Yellow', 'RPG', 'Game Boy')
lista = [jogo1, jogo2, jogo3]


app = Flask(__name__)
app.secret_key = 'vpaulo'


# criar rota e uma função 
@app.route('/')
def index():

    return render_template('lista.html', titulo='JOGOS', jogos=lista)

# rota novo cadastro
@app.route('/novo')
def novo():
    return render_template('novo.html', titulo='Novo Jogo')

#Rota para criar um novo jogo
@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console) # criando o objeto
    lista.append(jogo)
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo='Faça seu login')

@app.route('/autenticar', methods=['POST', ])
def autenticar():
    if 'alohomora' == request.form['senha']:
        session['logado'] = request.form['usuario']
        flash(session['logado'] + ' logado com sucesso')
        return redirect('/')
    else:
        flash('usuario não logado')
        return redirect('/login')
    
@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Logout efetuado com sucesso')
    return redirect('/')
    

app.run(debug=True) # debug faz o update automatico