from flask import Flask,request, redirect, Response, session
from flask_restful import Api,Resource

app=Flask(__name__)
app.secret_key ="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"
api=Api(app)

from controller.auth import Auth,Redirects
from controller.shop import CRUD
from controller.product import ProductCrud

# shopify CRUD OPERATIONS
api.add_resource(Auth,'/shopify')
api.add_resource(Redirects,'/shopify/callback')
api.add_resource(CRUD,'/shopify/products','/shopify/products/<string:id>')

#Mongodb CRUD OPERATIONS
api.add_resource(ProductCrud,'/api','/api/<string:id>')


if __name__=='__main__':
    app.run(debug=True,port=44368)