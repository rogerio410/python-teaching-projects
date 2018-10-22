"""
    to run:
    $ export FLASK_ENV=development
    $ export FLASK_APP=application.app.py
    $ flask run
"""
from flask import Flask, render_template, request, redirect, flash, session
from business.models import Repositorio, Arquivo


app = Flask(__name__)
app.secret_key = 'oi234'

# variáveis globais
repositorios = []


@app.route('/')
def index():
    return render_template('index.html', repositorios=repositorios)


@app.route('/git-init', methods=['post'])
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
            flash('Repo removido!')
    return redirect('/')


@app.route('/repositorio/<string:nome>')
def entrar_repositorio(nome):
    try:
        repositorio = obter_repositorio(por_nome=nome)
        session['repositorio'] = repositorio.nome
        return render_template('repositorio.html', repositorio=repositorio)
    except Exception as e:
        print(e)
        flash('Repositório inválido!', 'erro')
        return redirect('/')


@app.route('/sair-repositorio')
def sair_repositorio():
    session.clear()
    return redirect('/')


@app.route('/novo-arquivo', methods=['POST'])
def novo_arquivo():
    nome = request.form['nome']
    repositorio: Repositorio = obter_repositorio(por_nome=session.get('repositorio'))
    repositorio.novo_arquivo(nome)
    flash('Arquivo criado com sucesso!')
    return redirect('/repositorio/'+repositorio.nome)


@app.route('/git-add/<string:filename>')
def git_add(filename):
    repositorio: Repositorio = obter_repositorio(por_nome=session.get('repositorio'))
    repositorio.add(filename)
    flash('Git add Ok!')
    return redirect('/repositorio/' + repositorio.nome)


@app.route('/new-line/<string:filename>')
def nova_linha_arquivo(filename):
    repositorio: Repositorio = obter_repositorio(por_nome=session.get('repositorio'))
    arquivo: Arquivo = repositorio.buscar_arquivo(filename)
    arquivo.add_linha()
    return redirect('/repositorio/' + repositorio.nome)


def obter_repositorio(por_nome):
    repositorio = list(filter(lambda x: x.nome == por_nome, repositorios))
    return repositorio[0]