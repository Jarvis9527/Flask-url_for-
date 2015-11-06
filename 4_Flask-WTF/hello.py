#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, redirect, request, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

class NameForm(Form):
    Name = StringField('What is your name?', validators=[Required()])
    Password = PasswordField('Please input password', validators=[Required()])
    submit = SubmitField('Submit')
#validators指定一个由验证函数组成的列表，在接受用户提交数据之前验证数据。验证函数Required确保提交字段不为空

app = Flask(__name__)
app.config['SECRET_KEY'] = 'xiaosong'
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('base.html', form=form, name=name)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=7080)

