from database import db

class Sample(db.Model):
    __tablename__ = "sample"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    # first_name = db.Column(db.String(30))

    # deliveries = db.relationship('Delivery', backref='user')
    # roles = db.relationship(
    #     'Role', secondary='user_is_role', back_populates='users')

