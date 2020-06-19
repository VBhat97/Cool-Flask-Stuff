from flask import Flask,render_template,request,redirect,url_for
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html',name='Vaibhav')

@app.route("/your-url",methods=['GET','POST'])
def about():
    if request.method=='POST':
        url={}
        url[request.form['name']]={'url':request.form['code']}
        with open('urls.json','w') as url_file:
            json.dump(url,url_file)
        return render_template('url.html',code=request.form['code'])
    else:
        return redirect(url_for('home'))