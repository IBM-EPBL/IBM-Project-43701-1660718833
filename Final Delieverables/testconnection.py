import os
import re
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=b1bc1829-6f45-4cd4-bef4-10cf081900bf.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32304;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;PROTOCOL=TCPIP;UID=vsv60334;PWD=JAWPs1gz8WWAbsMX;", "", "")
from flask import Flask,  redirect,render_template, request, session, url_for
app = Flask(__name__)

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/blog')
def blog():
    return render_template('blog.html')

# @app.route('/flash')
# def flash():
#     return render_template('flash.html')

@app.route('/categori')
def categori():
    return render_template('categori.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/details')
def details():
    return render_template('details.html')

@app.route('/elements')
def elements():
    return render_template('elements.html')

@app.route('/latest_news')
def latest_news():
    return render_template('latest_news.html')
    
@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/single-blog')
def single_blog():
    return render_template('single-blog.html')

@app.route("/")
def navbar():
    return render_template("Nav.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route('/signup')
def signup():
    return render_template('signup.html')

# @app.route('/flash')
# def flash():
#     return render_template('flash.html') 
app.secret_key = 'a'
@app.route('/signin', methods=['GET', 'POST'])
def login():
    global userid
    msg = ''

    if request.method == 'POST':
        un = request.form['email']
        pd = request.form['psw']
        print(un, pd)
        sql = "SELECT * FROM USERDATA WHERE EMAIL=? AND PASSWORD=?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, un)
        ibm_db.bind_param(stmt, 2, pd)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            session['loggedin'] = True
            session['id'] = account['EMAIL']
            userid = account['EMAIL']
            session['username'] = account['USERNAME']
            msg = 'Logged in successfully !'

            return render_template("index.html")
        else:
            msg = 'Incorrect username / password !'
    return render_template('signin.html', msg=msg)

@app.route('/signup', methods=['POST', 'GET'])
def regis():
    mg = ''
    if request.method == "POST":
        username = request.form['uname']
        register = request.form['rollnumber']
        email = request.form['email']
        pw = request.form['psw']
        sql = 'SELECT * FROM USERDATA WHERE email =?'
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        acnt = ibm_db.fetch_assoc(stmt)
        print(acnt)

        if acnt:
            mg = 'Account already exits!!'

        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            mg = 'Please enter the avalid email address'
        elif not re.match(r'[A-Za-z0-9]+', username):
            ms = 'name must contain only character and number'
        else:
            insert_sql = 'INSERT INTO USERDATA (USERNAME,ROLLNUMBER,EMAIL,PASSWORD) VALUES (?,?,?,?)'
            pstmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(pstmt, 1, username)
            ibm_db.bind_param(pstmt, 2, register)
            ibm_db.bind_param(pstmt, 3, email)
            ibm_db.bind_param(pstmt, 4, pw)
            print(pstmt)
            ibm_db.execute(pstmt)
            mg = 'You have successfully registered click login!'
            return render_template("signin.html", meg=mg)

    # elif request.method == 'POST':
    #     msg = "fill out the form first!"
    # return render_template("signup.html", meg=mg)

if __name__=='__main__':
   port = int(os.environ.get('PORT',5000)) 
   app.run(port=port,host="0.0.0.0")  
