from projeto_final import app
from flask import render_template, redirect, url_for, request

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')

@app.route('/feed')
def feed():
    return render_template('feed.html')

@app.route('/criaranuncio')
def criaranuncio():
    return render_template('criaranuncio.html')

@app.route('/infoad')
def infoad():
    return render_template('infoad.html')

@app.route('/resetpass')
def resetpass():
    return render_template('resetpass.html')

