# libraries are imported
import os
from flask import Flask, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy

# template directory is used here as it contains the html page
# where user will input the text to be compared
template_dir = os.path.abspath('templates')
print("show the path of the template directory:", template_dir)

# app is the object of the class flask
app = Flask(
		__name__,
		template_folder=template_dir,
		
	)
# confiuration is done. Remember as data has to be inserted in mysql container
# there is no need to use localhost instead use db which is the mysql service mentioned in the
# docker compose file
# please read the docker compose file also
app.config['SECRET_KEY'] = 'anything'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123@db:3306/text_similarity'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# data base object is created using sqlalchemy
db = SQLAlchemy(app)
