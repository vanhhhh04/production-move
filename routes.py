from app import app, db
from models import Admin
from models import ManufactureFactory
from sqlalchemy import select
from flask import request


@app.route("/api/login", methods=["POST"])
def login():
	"""
	{
		"username": "admin",
		"password": "admin",
		"user_type": "ADMIN"
	}
	"""
	body = request.json

	if body["user_type"] == "ADMIN":
		user: Admin = db.session.execute(
			db.select(Admin).where(
				Admin.username == body["username"], 
				Admin.password == body["password"]
			)
		).scalar()
		return str(int(user.is_active))
	elif body["user_type"] == "MANUFACTURE_FACTORY":
		user: ManufactureFactory = db.session.execute(
			db.select(ManufactureFactory).where(
				ManufactureFactory.username == body["username"],
				ManufactureFactory.password == body["password"]
			)
		).scalar()
		return user.name

if __name__ == "__main__":
	app.run(debug=True)
