import sqlite3
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):  # every resource is a class.  Stuedent thee=reofre inherits Cla  Resource
    # @jwt_required()                               #  now parser belongs to the 'Item' class instead of repeated in th emethods
    parser = reqparse.RequestParser()           # only specific fiels passed via json payload to the endpoint
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be blank"
    )

    @jwt_required()
    def get(self, name):    #methods REsource is going to accept i.e. get# if no items in list return 'None'
        item = ItemModel.find_by_name(name)  # returns item object
        if item:
            return item.json()  #returns item itself
        return {'message': 'item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "item '{}' exists already".format(name)}, 400 # return a dictionary

        data = Item.parser.parse_args()  # checks the price

        item = ItemModel(name, data['price'])       # price keywd of data dictionary - ``#to python convert # json payload and correct Content Type header (Appln / jsom) is required to enalbe request.get_json() to work

        try:
            ItemModel.save_to_db()
        except:
            return {"message": "An error occurred inserting the item"}, 500

        return item.json(), 201

    def put(self, name):  # NB 'self' is used to associate this method (function) with the Class it belogs to e.g Class ITem
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)


        if item is None:
            item = ItemModel(name, data['price'])
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()

    def delete(self, name):
            item = ItemModel.find_by_name(name)
            if item:
                item.delete_from_db()

            return{'meassge': 'item deleted'}



class Itemlist(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.query.all()]}  #return all Itemlist
