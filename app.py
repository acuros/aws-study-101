import json
import random
import time

from threading import Thread

from flask import Flask, jsonify, request, Blueprint, abort
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://[username]:[password]@[host]/[dbname]'
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


def use_cpu():
    foo = 1
    for x in xrange(10000, 20000):
        foo *= x**3


def use_memory():
    def hold_memory():
        foo = ' ' * 100000000
        time.sleep(60)
    Thread(target=hold_memory).start()


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

    use_cpu()
    use_memory()

    q = db.session.query(User).filter(User.username == username)
    if db.session.query(q.exists()).scalar():
        abort(400)

    u = User(username, email)
    db.session.add(u)
    db.session.commit()
    return ''
