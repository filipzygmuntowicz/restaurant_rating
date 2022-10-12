from functions import rate_restaurant, get_rating_history, get_rating,\
    add_restaurant, db, app

with app.app_context():
    db.create_all()

add_restaurant("Test restaurant 1")
add_restaurant("Test restaurant 2")


def test(restaurant_id):
    rate_restaurant(restaurant_id, 50.21, 1, 3, 5)
    rate_restaurant(restaurant_id, 2.21, 3, 4, 3)
    rate_restaurant(restaurant_id, 63.21, 2, 1, 1)
    get_rating_history(restaurant_id)
    get_rating(restaurant_id)


print("Test restaurant 1")
test(1)
print("Test restaurant 2")
test(2)
