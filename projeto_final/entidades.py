from projeto_final import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), unique=True, nullable=False)
    sobrenome = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(1000), nullable=False)
    cidade = db.Column(db.String(100), nullable=False)
    estado = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(100), unique=True, nullable=False)
    complemento = db.Column(db.String(1000), nullable=False)
    nascimento = db.Column(db.String(1000), nullable=False)
    idade = db.Column(db.String(1000), nullable=False)
    foto = db.Column(db.String(1000), nullable=False)
    biografia = db.Column(db.String(1000), nullable=False)
