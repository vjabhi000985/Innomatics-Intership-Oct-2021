from flask import Flask,request,redirect
from flask.templating import render_template
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urls.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///user.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Urls(db.Model):
    id = db.Column("id",db.Integer,primary_key=True)
    original_url = db.Column("original_url",db.String())
    shorten_url = db.Column("shorten_url",db.String())

    def __init__(self,original_url,shorten_url):
        self.original_url = original_url
        self.shorten_url = shorten_url

class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    email = db.Column(db.String(120))
    password = db.Column(db.String(80))

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

#@app.before_first_request
#def delete_tables():
#    db.session.query(Urls).delete()
#    db.session.commit()

@app.before_first_request
def create_tables():
    db.create_all()

def short():
    letters = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    while True:
        rand_letters = random.choices(letters,k=6)
        rand_letters = "".join(rand_letters)
        short_url = Urls.query.filter_by(shorten_url=rand_letters).first()
        if not short_url:
            return rand_letters

@app.route('/')
def homeGet():
    return render_template('home.html')

@app.route('/',methods=['POST'])
def homePost():
    if request.method == "POST":
        received_url = request.form.get('ln')
        detected_url = Urls.query.filter_by(original_url=received_url).first()
        if detected_url:
            data = f"{detected_url.shorten_url}"
            return render_template('result.html',data=data)
        else:
            s_url = short()
            new_url = Urls(received_url,s_url)
            db.session.add(new_url)
            db.session.commit()
            return render_template('result.html',data=s_url)
    #data[shorten_url] = original_url
    else:
        return render_template('home.html')

@app.route('/history')
def historyGet():
    data = Urls.query.all()
    return render_template('history.html',data=data)

@app.route('/login',methods=["GET","POST"])
def login():
    if request.method == "POST":
        uname = request.form.get('uname')
        passw = request.form.get('passw')
        
        login = user.query.filter_by(username=uname, password=passw).first()
        if login is not None:
            user1 = user.query.filter_by(username=uname).first()
            return render_template('home.html',data=user1)
        else:
            return render_template("home.html")
    return render_template('login.html')

@app.route('/signup',methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        uname = request.form.get('uname')
        mail = request.form.get('mail')
        passw = request.form.get('passw')

        register = user(username = uname, email = mail, password = passw)
        db.session.add(register)
        db.session.commit()
        return render_template("login.html")
    return render_template("signup.html")

@app.route('/<url>')
def shortURL(url):
    long_url = Urls.query.filter_by(shorten_url=url).first()
    if long_url:
        return redirect(long_url.original_url)
    else:
        return "<h3>Page not found.Please check the url.</h3>"
    #if int(url) in data:
    #    return "Redirecting to {}".format(data[int(url)])
    #return "Incorrect URL"
    pass
if __name__=='__main__':
    app.run(debug=True)
