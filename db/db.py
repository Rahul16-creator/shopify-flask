from mongoengine import *

connect(
    db="shopify_flask",
    host="localhost",
    port=27017
)


class Products(DynamicDocument):
    id=IntField(primary_key=True)
    pass

