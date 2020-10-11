from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from pymongo import MongoClient
import bcrypt

app = Flask(__name__)
api = Api(app)

client = MongoClient("mongodb://localhost:27017")
db = client.sentence_api
users = db["users"]


def verify_log_info(username,password):
    try:
        hashed = users.find({
            "username": username
        })[0]["password"]
        if bcrypt.hashpw(password.encode("utf-8"),hashed) == hashed:
            return True
    except:
        return False
    


class register(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        try:
            if username == users.find({"username":username})[0]["username"]:
                retjson = {
                    "status" : 302,
                    "msg" : "Username already exists, try different one."
                }
                return retjson
        except:
            hashed = bcrypt.hashpw(password.encode("utf-8"),bcrypt.gensalt())
            users.insert({
                "username": username,
                "password": hashed,
                "sentence": [],
                "tokens" : 10
            })

            retjson = {
                "status" : 200,
                "msg" : "Registered Successfully."
            }

            return retjson

class store(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]
        sentence = data["sentence"]

        match = verify_log_info(username,password)

        if(match):
            all_data = users.find({"username":username})[0]
            prev_msg = all_data["sentence"]
            tokens = all_data["tokens"]
            if(tokens<1):
                retjson = {
                "status" : 305,
                "msg" : "Out of tokens, try to buy some."
                }
                return retjson
                
            prev_msg.append(sentence)
            users.update({
                    "username": username
                },{
                    "$set":{"sentence": prev_msg,"tokens": tokens-1}
                }
            )

            retjson = {
                "status" : 200,
                "msg" : "Sentence Inserted.",
                "tokens available" : tokens-1
            }
            return retjson
        else:
            retjson = {
                "status" : 301,
                "msg" : "Username or Password dosen't match."
            }
            return retjson

class view(Resource):
    def post(self):
        data = request.get_json()
        username = data["username"]
        password = data["password"]

        match = verify_log_info(username,password)

        if(match):
            all_data = users.find({"username":username})[0]
            msg = all_data["sentence"]
            tokens = all_data["tokens"]
            retjson = {
                "status" : 200,
                "tokes avialable" : tokens,
                "messeges": msg
            }
            return retjson
        else:
            retjson = {
                "status" : 301,
                "msg" : "Username or Password dosen't match."
            }
            return retjson




api.add_resource(register,"/register")  
api.add_resource(store,"/store")
api.add_resource(view,"/view")

if __name__=="__main__":
    app.run(host='localhost',debug = True)