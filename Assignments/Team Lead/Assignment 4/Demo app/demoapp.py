from flask import Flask,render_template
import os
app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")



if __name__=='__main__':
    port = int(os.environ.get('PORT',5000)) 
    app.run(port=port,host="0.0.0.0")

