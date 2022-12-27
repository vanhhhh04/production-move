from app import db, app
import sqlalchemy as sa


class Admin(db.Model):
	admin_id = sa.Column(sa.Integer, primary_key=True)
	username = sa.Column(sa.String(1000))
	password = sa.Column(sa.String(1000))
	created_at = sa.Column(sa.DateTime)
	updated_at = sa.Column(sa.DateTime)
	is_active = sa.Column(sa.Boolean)
	name = sa.Column(sa.String(1000))


class ManufactureFactory(db.Model):
	manufacture_factory_id = sa.Column(sa.Integer, primary_key=True)
	admin_id = sa.Column(sa.ForeignKey("admin.admin_id"))
	username = sa.Column(sa.String(1000))
	password = sa.Column(sa.String(1000))
	created_at = sa.Column(sa.DATETIME)
	update_at = sa.Column(sa.DateTime)
	is_active = sa.Column(sa.String(1000))
	name = sa.Column(sa.String(1000))
	address = sa.Column(sa.String(1000))
	phone_number = sa.Column(sa.INTEGER)


class DistributionAgent(db.Model):
	distribution_agent_id = sa.Column(sa.INTEGER, primary_key=True)
	admin_id = sa.Column(sa.ForeignKey("admin.admin_id"))
	username = sa.Column(sa.String(1000))
	password = sa.Column(sa.String(1000))
	created_at = sa.Column(sa.DATETIME)
	update_at = sa.Column(sa.DateTime)
	is_active = sa.Column(sa.String(1000))
	name = sa.Column(sa.String(1000))
	address = sa.Column(sa.String(1000))
	phone_number = sa.Column(sa.INTEGER)


class WarrantyCenter(db.Model):
	warranty_center_id  = sa.Column(sa.INTEGER, primary_key=True)
	admin_id = sa.Column(sa.ForeignKey("admin.admin_id"))
	username = sa.Column(sa.String(1000))
	password = sa.Column(sa.String(1000))
	created_at = sa.Column(sa.DATETIME)
	update_at = sa.Column(sa.DateTime)
	is_active = sa.Column(sa.String(1000))
	name = sa.Column(sa.String(1000))
	address = sa.Column(sa.String(1000))
	phone_number = sa.Column(sa.INTEGER)


class ProductLine(db.Model):
	product_line_id = sa.Column(sa.INTEGER, primary_key=True)
	name = sa.Column(sa.String(1000))
	created_at = sa.Column(sa.DateTime)
	updated_at = sa.Column(sa.DateTime)
	ram = sa.Column(sa.String(1000))
	screen = sa.Column(sa.String(1000))
	cpu = sa.Column(sa.String(1000))
	camera = sa.Column(sa.String(1000))
	pin = sa.Column(sa.String(1000))
	price = sa.Column(sa.String(1000))
	time_guarantee =sa.Column(sa.DATETIME)
	image_url = sa.Column(sa.String(1000))


if __name__ == "__main__":
	with app.app_context():
		user: Admin = db.session.execute(
				db.select(Admin).where(
					Admin.username == "admin", 
					Admin.password == "admin"
				)
			).scalar()
		

