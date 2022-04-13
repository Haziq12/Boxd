# myapp/__init__.py 

from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import os
from os import environ, path 
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

############################
###### DATABASE SETUP ######
############################


# set up connection to db
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost:5432/project4"
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('postgres://inzmwkizqctall:6b6a7cab0e8c260b93a50842817bdac736d45ddc57aceb3f7128d87d7138a1a0@ec2-52-21-136-176.compute-1.amazonaws.com:5432/d4rs0juolr9dsh').replace("://", "ql://", 1)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
db.init_app(app)
Migrate(app, db)


#############################

############ LOGIN CONFIGS ##############

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'





# Registering Blueprints - 

from myapp.core.views import core 
app.register_blueprint(core)

#linking the 404 and 403 error pages into the app 
from myapp.error_pages.handlers import error_pages
app.register_blueprint(error_pages)


#linking users views Blueprint
from myapp.users.views import users
app.register_blueprint(users)


# Linking and registering items views Blueprint
from myapp.items.views import items
app.register_blueprint(items)