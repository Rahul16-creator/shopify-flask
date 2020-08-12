from flask import Flask,request, redirect, Response, session
from flask_restful import Api,Resource
from  config import Config
import requests,json


class Auth(Resource):
    def get(self):
        if request.args.get('shop'):
            shop = request.args.get('shop')
        else:
            return Response(response="Error:parameter shop not found", status=500)

        auth_url = "https://{0}/admin/oauth/authorize?client_id={1}&scope={2}&redirect_uri={3}".format(
            shop, "d13dfe09e0bb1e563e20709ed6aae988", 'read_products, write_products,read_collection_listings',
            'https://3d931fb168f3.ngrok.io/shopify/callback'
        )


        return redirect(auth_url)


class Redirects(Resource):
    def get(self):
        if request.args.get("shop"):
           
            params = {
                "client_id": "d13dfe09e0bb1e563e20709ed6aae988",
                "client_secret": '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',
                "code": request.args.get("code")
            }

            resp = requests.post(
                "https://{0}/admin/oauth/access_token".format(
                    request.args.get("shop")
                ),
                data=params
            )

            if 200 == resp.status_code:
                resp_json = json.loads(resp.text)

                session['access_token'] = resp_json.get("access_token")
                session['shop'] = request.args.get("shop")

                return  session['access_token']
            else:
                return "Error in Auth"
