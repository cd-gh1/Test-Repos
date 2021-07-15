from flask import Flask
from flask_restful import Api    #flask_restful doesn't need jsonify as it does it automaticall i.e returns dictonaries
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister  # new resource added
from resources.item import Item, Itemlist
from resources.store import Store, Storelist
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # turns off flask_sqlalchemy extentions behaviour because SQLAlchemy is a better tracker
app.secret_key = 'secretp'
api = Api(app)


@app.before_first_request  # runs first
def create_tables():
    db.create_all()  # creates all tables in 'sqlite:///data.db'


jwt = JWT(app, authenticate, identity)  # /auth and send username and password.   initialise JWT object  to use aoo authenticate and identity

api.add_resource(Store, '/store/<string:name>')
api.add_resource(Item,'/item/<string:name>')  # how resourceis accessed
api.add_resource(Itemlist, '/items')
api.add_resource(Storelist, '/stores')
api.add_resource(UserRegister, '/register')  # when post request maded to /register it calls UserRegister
                                            # calls the post method function

if __name__ == '__main__': #only the file that you 'run' explicitly  is called main
#    from db import db
    db.init_app(app)
    app.run(port=8080, debug=True)  # now doesnot run when imported on systax checked when using 'import' command to call it
                                    # if not main then file has been imported
