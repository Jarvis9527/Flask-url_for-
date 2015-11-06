#!/usr/bin/env python 
#-*- coding:utf-8 -*- 

from flask import Flask, render_template, request, url_for, redirect, session 
from flask_bootstrap import Bootstrap
import MySQLdb as mysql 
import os 

app = Flask(__name__) 
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500


@app.route('/index/', methods=['GET', 'POST']) 
def index(): 
    if request.method == "POST": 
        username = request.form.get('username') 
        password = request.form.get('password') 
        user_dic = {} 
        conn1 = mysql.connect("127.0.0.1", "root", "123.com", "Flask") 
        cursor = conn1.cursor() 
        sql_select = "select * from user;" 
        try: 
            cursor.execute(sql_select) 
            data = cursor.fetchall() 
            for row in data: 
                user_name = row[1] 
                pass_word = row[2] 
                user_dic[user_name] = pass_word 
        except: 
            print "Error: unable to fetch data" 
        conn1.close() 
        for key, value in user_dic.items(): 
            if username == key and password == value: 
                return redirect('http://www.baidu.com')
            return redirect(url_for('index'))  #page_not_found

        conn = mysql.connect("127.0.0.1", "root", "123.com", "Flask") 
        cursor = conn.cursor() 
        sql = 'insert into Flask (username, password) values(%s, %s)' 
        try: 
            cursor.execute(sql, (username, password)) 
            conn.commit() 
        except: 
            cursor.rollback() 
        cursor.close() 
        conn.close() 
        return 'user is %s ok ! ' % (username,) 
    else: 
        return render_template('index.html') 


if __name__ == '__main__': 
    app.debug = True 
    app.run(host='0.0.0.0', port=7080) 
