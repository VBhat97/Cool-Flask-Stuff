from flask import Flask,render_template,request,redirect,url_for,flash
import json
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'h3ibhihgibhh132ujb'

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/your-url",methods=['GET','POST'])
def about():
    if request.method=='POST':
        url={}

        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                url=json.load(urls_file)

        if request.form['name'] in url.keys():
            flash('The name is already taken, sorry. Try another one.')
            return redirect(url_for('home'))

        if 'url' in request.form.keys():
            url[request.form['name']]={'url':request.form['code']}
        else:
            f=request.files['file']
            full_name=request.form['name'] + secure_filename(f.filename)
            f.save('C:/Users/V.Bhat/Desktop/Graduate Studies/Co-Corriculars/Projects/Cool-Flask-Stuff/'+full_name)
            url[request.form['name']]={'url':full_name}

        with open('urls.json','w') as url_file:
            json.dump(url,url_file)
        return render_template('url.html')
    else:
        return redirect(url_for('home'))

@app.route('/<string:code>')
def redirect_to_url(code):
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            url=json.load(urls_file)
            if 'url' in url[code].keys():
                return redirect(url[code]['url'])
    