from database import db


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return 'User: {}'.format(self.name)

# -----------


class Belonging(db.Model):
    __tablename__ = 'belonging'
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(100))
    description = db.Column(db.String(100))
    brand = db.Column(db.String(100))
    count = db.Column(db.Integer)
    price = db.Column(db.Integer)

    def __init__(self, category, description, brand, count, price):
        self.category = category
        self.description = description
        self.brand = brand
        self.count = count
        self.price = price

    def __repr__(self):
        return 'Belonging: {}'.format(self.description)
