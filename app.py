import json

from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://acuros:test1234@test-db.c6adtqxdporu.ap-northeast-1.rds.amazonaws.com/acuros'
db = SQLAlchemy(app)

from models import User

@app.route('/')
def user_list():
    users = []
    for u in User.query.all():
        users.append(dict(id=u.id, username=u.username, email=u.email))
    return jsonify(users=users)

if __name__ == '__main__':
    app.run()
