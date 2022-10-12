from setup import *


class Restaurant(db.Model):

    __tablename__ = 'Restaurants'
    restaurant_id = db.Column(db.Integer, primary_key=True)
    restaurant_name = db.Column(db.String)
    taste = db.Column(db.Float)
    size = db.Column(db.Float)
    service = db.Column(db.Float)
    earnings = db.Column(db.Float)

    def __init__(
        self, restaurant_name, taste,
        size, service, earnings
    ):
        self.restaurant_name = restaurant_name
        self.taste = taste
        self.size = size
        self.service = service
        self.earnings = earnings


class Rating(db.Model):

    __tablename__ = 'Ratings'
    rating_id = db.Column(db.Integer, primary_key=True)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('Restaurants'))
    db.relationship(
        "Restaurants", backref=db.backref("restaurant_ratings", uselist=False))
    bill_value = db.Column(db.Float)
    taste = db.Column(db.Float)
    size = db.Column(db.Float)
    service = db.Column(db.Float)
    date = db.Column(db.DateTime)

    def __init__(
        self, restaurant_id, bill_value, taste, size, service, date
    ):
        self.restaurant_id = restaurant_id
        self.bill_value = bill_value
        self.taste = taste
        self.size = size
        self.service = service
        self.date = date
