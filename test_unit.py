import shutil
import os

shutil.copyfile('configprod.txt', 'configprodcopy.txt')

try:
    with open('configprod.txt', 'w') as f:
        f.write(open('configtest.txt', 'r').read())
except FileNotFoundError:
    print("Test database config not found. Please provide necessary details.\nDatabase url:")
    db_url = input()
    print("Name of database:")
    db_name = input()
    print("Database username:")
    db_username = input()
    print("Database password:")
    db_password = input()
    sql_test_credentials = 'postgresql://{}:{}@{}/{}'.format(
            db_username, db_password, db_url, db_name)
    with open('configtest.txt', 'w') as f:
        f.write(sql_test_credentials)
    with open('configprod.txt', 'w') as f:
        f.write(sql_test_credentials)

# IT"S NECESSARY FOR THE TESTS TO WORK CORRECTLY TO IMPORT IT
# HERE INSTEAD OF ON TOP EVEN THO IT'S NOT RECOMMENDED BY PEP8
from functions import rate_restaurant, get_rating_history, get_rating,\
    add_restaurant, db, app, Restaurant, Rating, datetime

with app.app_context():
    db.drop_all()
    db.create_all()


class Test:

    def test_add_restaurant(self):
        add_restaurant("Test restaurant 1")
        with app.app_context():
            restaurant = Restaurant.query.filter_by(
                        restaurant_name="Test restaurant 1").first()
            assert restaurant.restaurant_name == "Test restaurant 1"

    def test_rate_restaurant(self):
        add_restaurant("Test restaurant 2")
        rate_restaurant(2, 50.21, 1, 3, 5)
        with app.app_context():
            restaurant = Restaurant.query.filter_by(
                        restaurant_id=2).first()
            assert restaurant.taste == -50.21 and restaurant.size == 50.21 and\
                restaurant.service == 150.63 and\
                restaurant.earnings == 50.21

    def test_get_rating_history(self):
        add_restaurant("Test restaurant 3")
        rate_restaurant(3, 50.21, 1, 3, 5)
        history = get_rating_history(3)[0]
        assert history['taste'] == 1.0 and history['size'] == 3.0 and\
            history['service'] == 5.0

    def test_get_rating(self):
        add_restaurant("Test restaurant 4")
        rate_restaurant(4, 50.21, 1, 3, 5)
        taste, size, service, mean = get_rating(4)
        assert taste == {
            'category': 'taste', 'float': -50.21, 'string': '*'} and\
            size == {'category': 'size', 'float': 50.21, 'string': '***'} and\
            service == {
                'category': 'service', 'float': 150.63, 'string': '*****'} and\
            mean == {'category': 'mean', 'float': 50.21, 'string': '***'}


shutil.copyfile('configprodcopy.txt', 'configprod.txt')
os.remove('configprodcopy.txt')
