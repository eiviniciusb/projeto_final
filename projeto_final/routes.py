from projeto_final import app
from flask import render_template, redirect, url_for, request

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
    nome = request.form['cad_nome']
    sobrenome = request.form['cad_sobrenome']
    senha = request.form['cad_senha']
    email = request.form['cad_email']
    cidade = request.form['cad_cidade']
    estado = request.form['cad_estado']
    endereco = request.form['cad_endereco']
    complemento = request.form['cad_complemento']
    return redirect('/infoad')

@app.route('/forminfo', methods=['POST'])
def forminfo():
    data_nascimento = request.form['nascimento']
    idade = request.form['idade']
    usuario = request.form['tipo_usuario']
    foto = request.form['foto_perfil']
    bio = request.form['biografia']
    return redirect('/infoad')

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
