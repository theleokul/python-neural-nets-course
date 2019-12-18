from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy  # ORM - Object-Relational Mapping
from flask_marshmallow import Marshmallow  # Serialization and deserialization procedures
import os

# This part create an instances of our web application and set path of our SQLite uri.
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'crud.sqlite')

# On this part we binding SQLAlchemy and Marshmallow into our flask application.
db = SQLAlchemy(app)
ma = Marshmallow(app)


# Here we declare model called User and defined its field with it’s properties.
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email


# This part defined structure of response of our endpoint.
# We want that all of our endpoint will have JSON response.
# Here we define that our JSON response will have two keys(username, and email).
class UserSchema(ma.Schema):
    class Meta:
        # Fields to expose
        fields = ('username', 'email')


# Also we defined user_schema as instance of UserSchema, and user_schemas as instances of list of UserSchema.
user_schema = UserSchema()
users_schema = UserSchema(many=True)


# On this part we define endpoint to create new user.
# First we set the route to “/user” and set HTTP methods to POST.
# After set the route and methods we define function that will executed if we access this endpoint.
# On this function first we get username and email from request data.
# After that we create new user using data from request data.
# Last we add new user to data base and show new user in JSON form as response.
@app.route("/user", methods=["POST"])
def add_user():
    username = request.json['username']
    email = request.json['email']
    new_user = User(username, email)

    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)


# On this part we define endpoint to get list of all users and show the result as JSON response.
@app.route("/user", methods=["GET"])
def get_user():
    all_users = User.query.all()

    return users_schema.jsonify(all_users)


# Like on previous part on this part we define endpoint to get user data,
# but instead of get all the user here we just get data from one user based on id.
@app.route("/user/<id>", methods=["GET"])
def user_detail(id):
    user = User.query.get(id)

    return user_schema.jsonify(user)


# On this part we define endpoint to update user.
# First we call user that related with given id on parameter.
# Then we update username and email value of this user with value from request data.
@app.route("/user/<id>", methods=["PUT"])
def user_update(id):
    user = User.query.get(id)
    username = request.json['username']
    email = request.json['email']

    user.email = email
    user.username = username
    db.session.commit()

    return user_schema.jsonify(user)


# Last we define endpoint to delete user. First we call user that related with given id on parameter. Then we delete it.
@app.route("/user/<id>", methods=["DELETE"])
def user_delete(id):
    user = User.query.get(id)

    db.session.delete(user)
    db.session.commit()

    return user_schema.jsonify(user)


if __name__ == '__main__':
    app.run(debug=True)
