from flask import Flask,request, redirect, Response, session
from flask_restful import Api,Resource

from config import Config
import requests,json



class CRUD(Resource):

    def get(self):
    
        headers = {
            "X-Shopify-Access-Token":"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",
            "Content-Type": "application/json"
        }

        url='https://shop-url.myshopify.com/admin/products.json'
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            products = json.loads(response.text)
            return products
        else:
            return False



    def post(self):

       data=request.get_json()
       new_product = {
       
            "product": {
            "title": data['title'],
            "body_html": data['body_html'],
            "product_type": data['product_type'],
            "Trackquantity":data['Trackquantity'],
            "variants": [
                {
                    "option1": data['option1'],
                    "price": data['price1'],
                    "inventory_management":"shopify",
                    "weight":data['weight1'],
                    "weight_unit":data['weight_unit1'],
                    "inventory_quantity":data['inventory_quantity1'],
                },
                {
                    "option1": data['option2'],
                    "price": data['price2'],
                    "weight":data['weight1'],
                    "inventory_management":"shopify",
                    "weight_unit":data['weight_unit1'],
                    "inventory_quantity":data['inventory_quantity2'],
                }
                ]
            }
        
         }
       url='https://shop-url.myshopify.com/admin/products.json'
       headers = {
            "X-Shopify-Access-Token": "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",
            "Content-Type": "application/json"
        }

       response = requests.post(url,json=new_product,headers=headers)
       print(response.status_code)
       if response.status_code == 201:
          products = json.loads(response.text)
          return products
       else:
         return False





    def put(self,id):

       data=request.get_json()
       new_product = {
       
            "product": {
            "title": data['title'],
            "body_html": data['body_html'],
            "product_type": data['product_type'],
            "Trackquantity":data['Trackquantity'],
            "variants": [
                {
                    "option1": data['option1'],
                    "price": data['price1'],
                    "inventory_management":"shopify",
                    "weight":data['weight1'],
                    "weight_unit":data['weight_unit1'],
                    "inventory_quantity":data['inventory_quantity1'],
                },
                {
                    "option1": data['option2'],
                    "price": data['price2'],
                    "weight":data['weight1'],
                    "inventory_management":"shopify",
                    "weight_unit":data['weight_unit1'],
                    "inventory_quantity":data['inventory_quantity2'],
                }
                ]
            }
        
         }
    

       

   
       url='https://shop-url.myshopify.com/admin/products/'+ id +'.json'
       headers = {
            "X-Shopify-Access-Token": "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",
            "Content-Type": "application/json"
        }

       response = requests.put(url,json=new_product,headers=headers)
       print(response.status_code)
       if response.status_code == 200:
          products = json.loads(response.text)
          return products
       else:
         return False

    def delete(self,id):

         url='https://shop-url.myshopify.com/admin/products/'+ id +'.json'
         headers = {
            "X-Shopify-Access-Token":"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",
            "Content-Type": "application/json"
        }

         response = requests.delete(url,headers=headers)
         print(response.status_code)
         if response.status_code == 200:
            
            return "item Deleted"
         else:
           return False


