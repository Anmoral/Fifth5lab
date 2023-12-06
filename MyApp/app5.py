import requests
from flask import Flask, render_template, request, redirect
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

cursor.executemany('''INSERT INTO users (username, login, password) VALUES (?, ?, ?)''', users_mas)

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST' and request.form.get("login"):
        username = request.form.get('username')
        password = request.form.get('password')
        cursor.execute("SELECT * FROM service.users WHERE login=%s AND password=%s", (str(username), str(password)))
        records = list(cursor.fetchall())
        return render_template('account.html', username=records[0][1])
    elif request.form.get("registration"):
        return redirect("/registration/")
    return render_template('login.html')

@app.route('/registration/', methods=['POST', 'GET'])
def registration():
    if request.method == 'POST':
        name = request.form.get('name')
        login = request.form.get('login')
        password = request.form.get('password')
        cursor.execute('INSERT INTO service.users (username, login, password) VALUES (%s, %s, %s);', (str(name), str(login), str(password)))
        connection.commit()
        return redirect('/login/')
        return render_template('registration.html')


result = connection.execute('''SELECT * from users WHERE username='123' AND password='1323' ''').fetchall()

print(result)