from orm_objects import Restaurant, Rating, db, app
from datetime import datetime


def add_restaurant(restaurant_name):
    with app.app_context():
        new_restaurant = Restaurant(
            restaurant_name=restaurant_name, taste=0, size=0, service=0,
            earnings=0)
        db.session.add(new_restaurant)
        db.session.commit()


def update_ratings(
        restaurant, taste_factor, size_factor, service_factor, bill_value):
    new_rating_taste = restaurant.taste + taste_factor*bill_value
    new_rating_size = restaurant.size + size_factor*bill_value
    new_rating_service = restaurant.service + service_factor*bill_value
    restaurant.taste = new_rating_taste
    restaurant.size = new_rating_size
    restaurant.service = new_rating_service
    restaurant.earnings = restaurant.earnings + bill_value
    return restaurant


def rate_restaurant(restaurant_id, bill_value, taste, size, service):
    try:
        bill_value = float(bill_value)
        taste = float(taste)
        size = float(size)
        service = float(service)
        with app.app_context():
            if taste > 5 or size > 5 or service > 5 or\
                    taste < 1 or size < 1 or service < 1:
                print("Invalid number of stars")
            else:
                taste = taste - 2
                size = size - 2
                service = service - 2
                restaurant = Restaurant.query.filter_by(
                    restaurant_id=restaurant_id).first()
                if restaurant is not None:
                    restaurant = update_ratings(
                        restaurant, taste, size, service, bill_value)
                    db.session.add(restaurant)
                    db.session.commit()
                    restaurant_id = restaurant.restaurant_id
                    new_rating = Rating(
                        restaurant_id=restaurant_id, bill_value=bill_value,
                        taste=taste, size=size, service=service,
                        date=datetime.now())
                    db.session.add(new_rating)
                    db.session.commit()
                else:
                    print("Restaurant not found in database.")
    except ValueError:
        print("Provided rates are not numbers!")


def get_rating_history(restaurant_id):
    with app.app_context():
        ratings = Rating.query.filter_by(
            restaurant_id=restaurant_id).all()
        if ratings is not None:
            for rating in ratings:
                print(
                    {
                        "taste": rating.taste + 2,
                        "size": rating.size + 2,
                        "service": rating.service + 2,
                        "date": datetime.strftime(
                            rating.date, "%Y-%m-%d %H:%M")
                    }
                )
        else:
            print("Rating history not found for a given restaurant.")


def stars_out_of_rating_points(rating_points, earnings):
    return "*" * (int(round(rating_points/earnings)) + 2)


def get_rating(restaurant_id):
    with app.app_context():
        restaurant = Restaurant.query.filter_by(
            restaurant_id=restaurant_id).first()
    if restaurant is not None:
        print(
            {
                "category": "taste",
                "float": round(restaurant.taste, 2),
                "string": stars_out_of_rating_points(
                    restaurant.taste, restaurant.earnings)
            }
        )
        print(
            {
                "category": "size",
                "float": round(restaurant.size, 2),
                "string": stars_out_of_rating_points(
                    restaurant.size, restaurant.earnings)
            }
        )
        print(
            {
                "category": "service",
                "float": round(restaurant.service, 2),
                "string": stars_out_of_rating_points(
                    restaurant.service, restaurant.earnings)
            }
        )
    else:
        print("Restaurant not found.")
