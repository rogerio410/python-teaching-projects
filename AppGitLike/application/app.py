"""
    to run:
    $ export FLASK_ENV=development
    $ export FLASK_APP=application.app.py
    $ flask run
"""
from flask import Flask, render_template, request, redirect, flash, session
from business.models import Repositorio


app = Flask(__name__)
app.secret_key = 'oi234'

# variáveis globais
repositorios = []


@app.route('/')
def index():
    return render_template('index.html', repositorios=repositorios)


@app.route('/novo-repositorio', methods=['post'])
def novo_repositorio():
    nome = request.form['nome']

    if nome not in [r.nome for r in repositorios]:
        repositorio = Repositorio(nome)
        repositorios.append(repositorio)
        flash('Repo criado com sucesso!')
    else:
        flash('Já existe um Repo com este nome', 'erro')
    return redirect('/')


@app.route('/apagar-repositorio/<string:nome>')
def apagar_repositorio(nome):
    for r in list(repositorios):
        if r.nome == nome:
            repositorios.remove(r)
    return redirect('/')


@app.route('/repositorio/<string:nome>')
def entrar_repositorio(nome):
    try:
        repositorio = obter_repositorio(por_nome=nome)
        session['repositorio'] = repositorio.nome
        flash('Repositório selecionado')
        return render_template('repositorio.html', repositorio=repositorio)
    except:
        flash('Repositório inválido', 'erro')
        return redirect('/')


@app.route('/sair-repositorio')
def sair_repositorio():
    session.clear()
    return redirect('/')


def obter_repositorio(por_nome):
    repositorio = list(filter(lambda x: x.nome == por_nome, repositorios))[0]
    return repositorio