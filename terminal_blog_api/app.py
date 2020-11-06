from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from database import Database
from module.user import Users

# basic initialization
app = Flask(__name__)
api = Api(app)
Database.initialize("Blogs")


# new user
u1 = Users(author="Fardaws Hassan",discription="A student.")

# creating post
u1.new_post(title="test title one",date="15081975",content="test content one.")
u1.new_post(title="test title two",date="15071973",content="test content two.")


if __name__=="__main__":
    app.run(host='localhost',debug = True)