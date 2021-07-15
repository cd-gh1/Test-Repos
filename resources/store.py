from flask_restful import Resource, reqparse
from models.store import StoreModel


class Store(Resource):  # every resource is a class.  Stuedent thee=reofre inherits Cla  Resource
    def get(self, name):    #methods REsource is going to accept i.e. get# if no items in list return 'None'
        store = StoreModel.find_by_name(name)  # returns item object
        if store:
            return store.json()  #returns item itself
        return {'message': 'Store not found'}, 404

    def post(self, name):
        if StoreModel.find_by_name(name):
            return {'message': "store '{}' exists already".format(name)}, 400 # return a dictionary

        store = StoreModel(name) # **data is same as data['price'], data['store_id]'])       # price keywd of data dictionary - ``#to python convert # json payload and correct Content Type header (Appln / jsom) is required to enalbe request.get_json() to work

        try:
            store.save_to_db()
        except:
            return {"message": "An error occurred creating the store"}, 500

        return store.json(), 201

    def delete(self, name):
            store = StoreModel.find_by_name(name)
            if store:
                store.delete_from_db()

            return{'message': 'store deleted'}


class Storelist(Resource):
    def get(self):
        return {'stores': [store.json() for store in StoreModel.query.all()]}  #return all Itemlist
