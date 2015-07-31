import json

from flask import Flask, jsonify, request, Blueprint
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://acuros:test1234@test-db.c6adtqxdporu.ap-northeast-1.rds.amazonaws.com/acuros'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(150), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

@app.route('/')
def user_list():
    users = []
    for u in User.query.all():
        users.append(dict(id=u.id, username=u.username, email=u.email))
    return jsonify(users=users)

@app.route('/add', methods=['POST'])
def add_user():
    username = request.form['username']
    email = request.form['email']
    u = User(username, email)
    db.session.add(u)
    db.session.commit()
    return ''
