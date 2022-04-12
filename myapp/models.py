#models 
from re import S
from myapp import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
#allows to set up isAuthenticate etc 
from flask_login import UserMixin
from datetime import datetime

#login management 
# allows us to use this in templates for isUser stuff 
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    country = db.Column(db.String(64))
    password_hash = db.Column(db.String(128))
    items = db.relationship('Item', backref='author', lazy=True)

    def __init__(self, email, username, password, country):
        self.email = email
        self.username = username
        self.country = country
        self.password_hash = generate_password_hash(password)

#going to use this in our login view 
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"Username {self.username}"


class Item(db.Model):
    __tablename__='items'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    itemName = db.Column(db.String(), nullable=False)
    itemDescription = db.Column(db.String(), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    condition = db.Column(db.String(), nullable=False)
    size = db.Column(db.String(), nullable=True)
    contactInfo = db.Column(db.String(), nullable=False)
    category = db.Column(db.String(), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    def __init__(self, itemName, itemDescription, price, condition, size, contactInfo, category, user_id):
        self.itemName = itemName
        self.itemDescription = itemDescription
        self.price = price
        self.condition = condition
        self.size = size
        self.contactInfo = contactInfo
        self.category = category
        self.user_id = user_id

    def __repr__(self):
        return f'Item ID: {self.id} -- Date: {self.date} -- itemName: {self.itemName} -- itemDescription: {self.itemDescription} -- price: {self.price} -- condition: {self.condition} -- size: {self.size} -- contactInfo: {self.contactInfo} -- category: {self.category}'
