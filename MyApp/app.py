import requests
from flask import Flask, render_template, request
import psycopg2
import sqlite3

app = Flask(__name__)
connection = sqlite3.connect('./service_db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
username TEXT NOT NULL,
login TEXT NOT NULL,
password VARCHAR NOT NULL
)
''')

users_mas = [('FEwsf', 'wfwefw', 323525),
             ('123', 'tryrtye', 1323),
             ('rhrhr', 'dfghdh', 5677),
             ('rhehd', 'bfbdcgd', 36563),
             ('FEdhtrdsf', 'fhghfh', 56757),
             ('dhgfh', 'fhghfgf', 768678),
             ('FEwdhsf', 'fhgghfh', 35377),
             ('dhgf', 'fhg', 8679),
             ('123', 'dghhf', 1323),
             ('dhgfh', 'dfhghd', 1323)]

cursor.executemany('''INSERT INTO users (username, login, password) VALUES (?, ?, ?, ?)''', users_mas)

@app.route('/', methods = ['GET', 'POST'])
def form_example():
    conn = sqlite3.connect('./service_db')
    # POST requests
    if request.method == 'POST':
        try:
            username = request.form.get('username')
            if len(username) == 0:
                return '''<h3>Вернитесь и введите имя</h3>'''
            password = request.form.get('password')
            if len(password) == 0:
                return '''<h3>Введите пароль</h3>'''
            result = conn.execute('''SELECT username from users WHERE username={} and password={}'''.format(username, password)).fetchall()[0][0]
            print(len(result))
            return '''
                        <h3>
                        Добро пожаловать, {}
                        </h3>
                        '''.format(result)
        except:
            return '''<h3>Такой учетной записи нет</h3>'''

    # GET request
    return '''
           <form method="POST">
               <div><label>username: <input type="text" name="username"></label></div>
               <div><label>password: <input type="password" name="password"></label></div>
               <input type="submit" value="Submit">
           </form>
           
           '''

result = connection.execute('''SELECT * from users WHERE username='123' AND password='1323' ''').fetchall()

print(result)