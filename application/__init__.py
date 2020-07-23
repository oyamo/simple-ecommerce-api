from flask import Flask
app = Flask(__name__)

# Configs incase any database issues needed
# app.secret_key= "hdkdkdsj"
# app.config.from_object(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

from application import services

