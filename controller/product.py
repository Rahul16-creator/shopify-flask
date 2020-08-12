from flask import Flask,request, redirect, Response, session
from flask_restful import Api,Resource

from config import Config
import requests,json
from db.db import Products



class ProductCrud(Resource):

    def get(self):
        headers = {
            "X-Shopify-Access-Token":"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",
            "Content-Type": "application/json"
        }
        url='https://shop-url.myshopify.com/admin/products.json'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            products = json.loads(response.text)
            for item in products['products']:
                Products(**item).save()
            return "Item saved!!"
        else:
            return False



    def put(self,id):
       data=request.get_json()
       print(data)
       try:
           product=Products.objects(id=int(id)).get()
           product.update(**data)
           return "Item Updated Successfully"
       except DoesNotExist:
           return "Item does not found"


   
    def delete(self,id):
      try:
        product = Products.objects(id=int(id)).get()
        product.delete()
        return "Item Deleted Successfully"
      except DoesNotExist:
        return "Item does not found"
