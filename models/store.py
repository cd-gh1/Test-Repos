from db import db

class StoreModel(db.Model):   # Internal usage i.e not like a resource that is called by an endpoint
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    items = db.relationship('ItemModel', lazy='dynamic')  # allows a store to see what items are in the items database
                                          # a list of item models lazy, do not create an object ofr each item whenever a StoreModel is created - so can be expensive computationally
    def __init__(self, name):
        self.name = name
        # self.price = price

    def json(self):
        return {'name': self.name, 'items': [item.json() for item in self.items.all()]}  # dictionary representing item

    @classmethod
    def find_by_name(cls, name):
            return cls.query.filter_by(name=name).first()     # returns first row only

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
