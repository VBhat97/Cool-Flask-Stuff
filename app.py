from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html',name='Vaibhav')

@app.route("/your-url")
def about():
    return render_template('url.html',code=request.args['code'])