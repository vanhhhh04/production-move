from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:1922002@localhost/production_move"
db.init_app(app)

