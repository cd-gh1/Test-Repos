from db import db

class ItemModel(db.Model):   # Internal usage i.e not like a resource that is called by an endpoint
    __tablename__ = 'items'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    price = db.Column(db.Float(precision=2))

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))  # stores is table name and id is column
    store = db.relationship('StoreModel')  # can find a 'store_id in the database StoreModel'


    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {'name': self.name, 'price': self.price}  # dictionary representing item

    @classmethod
    def find_by_name(cls, name):
            return cls.query.filter_by(name=name).first()     # returns first row only

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
