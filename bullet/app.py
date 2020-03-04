"""
This is Nether.
Welcome to my world.
address: www.nether.ink
"""
import json
import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class BulletScreen(db.Model):
    id = Column(Integer, primary_key=True, autoincrement=True)
    author = Column(String(30), default='未名')
    message = Column(Text)


@app.route('/')
def get_bullet():
    bullets = BulletScreen.query.all()
    return render_template('getbullet.html', bullets=bullets)


@app.route('/setbullet', methods=['GET', 'POST'])
def set_bullet():
    if request.method == 'POST':
        author = request.form.get('author')
        message = request.form.get('message')
        bullet = BulletScreen(message=message, author=author)
        db.session.add(bullet)
        db.session.commit()
    return render_template('setbullet.html')


if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=80)
