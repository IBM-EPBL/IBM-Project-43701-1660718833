from flask import Flask, redirect,render_template, request, url_for
app = Flask(__name__)

# @app.route("/")
# def homepage():
#     return render_template("signup.html")

@app.route("/")
def navbar():
    return render_template("Nav.html")

@app.route("/signin")
def signin():
    return render_template("signin.html")

@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route("/login",methods=['POST'])
def send_data():
    username = request.form['uname']
    rollnumber = request.form['roll']
    email = request.form['email']
    password = request.form['psw']
    if(email == "gan@123.com" and rollnumber =="123" and username=="gan" and password=="gan123"):
        return render_template("homepage.html")
    else:
        print("error")


if __name__=='__main__':
    app.run(debug=True)



