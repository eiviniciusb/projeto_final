from flask import render_template, redirect, url_for, request, current_app as app

from datetime import datetime

from projeto_final import db
from projeto_final.entidades import Usuario

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/infoad')
def infoad():
    return render_template('infoad.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/perfilvoluntario')
def perfilvoluntario():
    return render_template('perfil_voluntario.html')

@app.route('/feedvoluntario')
def feedvoluntario():
    return render_template('feed_voluntario.html')

@app.route('/anuncio')
def anuncio():
    return render_template('anuncio.html')

@app.route('/feednaovoluntario')
def feednaovoluntario():
    return render_template('feed_nao_voluntario.html')

@app.route('/perfilnaovoluntario')
def perfilnaovoluntario():
    return render_template('perfil_nao_voluntario.html')

@app.route('/criaranuncio')
def criaranuncio():
    return render_template('criaranuncio.html')

@app.route('/contsuccess')
def contsuccess():
    return render_template('contsuccess.html')

@app.route('/logar', methods=['POST'])
def logar():
    email_da_pessoa = request.form['e_user']
    senha = request.form['pass_user']
    lembrar = request.form['lembrar']
    return redirect('/login')

@app.route('/formcadastro', methods=['POST'])
def formcadastro():
    nome_c = request.form['cad_nome']
    sobrenome_c = request.form['cad_sobrenome']
    senha = request.form['cad_senha']
    email_c = request.form['cad_email']
    cidade_c = request.form['cad_cidade']
    estado_c = request.form['cad_estado']
    endereco_c = request.form['cad_endereco']
    complemento_C = request.form['cad_complemento']
    
    alguem = Usuario.query.filter_by(nome=nome_c).first()
    
    if alguem is not None:
        session['mensagem'] = 'Usuário já cadastrado'
        return redirect('/cadastro')
    else:
        novo = Usuario()
        novo.nome = nome_c
        novo.sobrenome = sobrenome_c
        novo.senha = senha
        novo.email = email_c
        novo.cidade = cidade_c
        novo.estado = estado_c
        novo.endereco = endereco_c
        novo.complemento = complemento_C

        db.session.add(novo)
        db.session.commit()

        return redirect('/infoad')

@app.route('/forminfo', methods=['POST'])
def forminfo():
    data_nascimento = request.form['nascimento']
    idade = request.form['idade']
    usuario = request.form['tipo_usuario']
    foto = request.form['foto_perfil']
    bio = request.form['biografia']

    alguem = Usuario.query.filter_by(nome=nome_c).first()
    
    if alguem is not None:
        session['mensagem'] = 'Usuário já cadastrado'
        return redirect('/cadastro')
    else:
#        novo = Usuario()
        novo.nascimento = data_nascimento
        novo.idade = idade
        novo.foto = foto
        novo.biografia = bio

        db.session.add(novo)
        db.session.commit()

        return redirect('/sucess')

@app.route('/formcriaranuncio', methods=['POST'])
def formcriaranuncio():
    titulo = request.form['titulo_anuncio']
    imagem = request.form['imagem_anuncio']
    email = request.form['email_contato']
    telefone = request.form['telefone_contato']
    return redirect('/feednaovoluntario')

@app.route('/formcontact', methods=['POST'])
def formcontact():
    nome = request.form['cont_nome']
    assunto = request.form['cont_assunto']
    email = request.form['cont_email']
    mensagem = request.form['cont_mensagem']
    return redirect('/contsuccess')
