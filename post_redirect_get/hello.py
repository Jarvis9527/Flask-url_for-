#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import Required

class NameForm(Form):
    Name = StringField("What your name", validator=[Required()])
    Password = PasswordField("Please input password", validator=[Required()])
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

@app.route('/', methods=['GET','POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        return redirect(url_for('index'))
    return render_template('index.html', form=form, name=session.get('name'))

    

