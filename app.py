from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html',name='Vaibhav')

@app.route("/your-url",methods=['GET','POST'])
def about():
    if request.method=='POST':
        return render_template('url.html',code=request.form['code'])
    else:
        return "This is not allowed"