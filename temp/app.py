from mongoengine import *
from flask import Flask
from flask_restful import Api,Resource
import os

app=Flask(__name__)
api=Api(app)

connect(
    db="demo",
    host="127.0.0.1",
    port=27017
)

class User(Document):
    id=IntField(primary_key=True)
    username=StringField(required=True)
    email = EmailField(required=True,unique=True)
    password = BinaryField(required=True)

class Insert(Resource):
    def get(self):
        User(id= 2345676543234, username="raul", email="rahuls@gmail.com", password=os.urandom(16)).save()
        return "saved!!"

    def post(self):
        user=User.objects(username="raul")
        
        print(user)
        return "success!"


api.add_resource(Insert,'/')

app.run(debug=True)

