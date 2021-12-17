from flask import Flask, render_template, request, redirect, jsonify
from flask.json import jsonify 
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///nitu.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Nitu(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(200), nullable=False)
    last_name = db.Column(db.String(200), nullable=False)
    company_name = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(200), nullable=False)
    state = db.Column(db.String(200), nullable=False)
    zip = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(200), nullable=False)
    web = db.Column(db.String(200), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    
@app.route('/')
def home():    
    return render_template ('index.html')

@app.route('/user-GET', methods=['GET','POST'])
def list_user():
    user = Nitu()
    all_user = Nitu.query.all()
    return render_template ('get-user.html', all_user=all_user)
    # return render_template ('get-user.html', user=user, all_user=all_user)

@app.route('/user-POST', methods=['GET','POST'])
def post_user():
    if request.method == 'POST':
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        company_name=request.form['company_name']
        city=request.form['city']
        state=request.form['state']
        zip=request.form['zip']
        email=request.form['email']
        web=request.form['web']
        age=request.form['age']
        user = Nitu( first_name = first_name, last_name = last_name, company_name = company_name, city = city, state = state, zip = zip, email = email, web = web, age = age)
        db.session.add(user)
        db.session.commit()
    
        
        return redirect('/user-GET')
    all_user = Nitu.query.all()
    return render_template ('post-user.html', all_user=all_user)


@app.route('/user-GET/<int:user_id>', methods=['GET','POST'])
def find_user(user_id):
    user = Nitu.query.filter_by(user_id=user_id).first()
    return render_template ('find-user.html', user=user)

@app.route('/user-PUT/<int:user_id>', methods=['GET','POST'])
def update_user(user_id):
    if request.method == 'POST':
        first_name=request.form['first_name']
        last_name=request.form['last_name']
        company_name=request.form['company_name']
        city=request.form['city']
        state=request.form['state']
        zip=request.form['zip']
        email=request.form['email']
        web=request.form['web']
        age=request.form['age']
        user = Nitu.query.filter_by(user_id=user_id).first()
        user.first_name = first_name
        user.last_name = last_name
        user.company_name = company_name
        user.city = city
        user.state = state
        user.zip = zip
        user.email = email
        user.web = web
        user.age = age
        db.session.add(user)
        db.session.commit()
        return redirect ('/user-GET')
    
    
    user = Nitu.query.filter_by(user_id=user_id).first()
    return render_template ('put-user.html', user=user)

@app.route('/user-DELETE/<int:user_id>', methods=['GET','POST'])
def delete_user(user_id):
    user = Nitu.query.filter_by(user_id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect("/user-GET")

if __name__ =='__main__':
    app.run(debug=True)