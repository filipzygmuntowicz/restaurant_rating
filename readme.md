# PREQUISITES:

You need to install the required libraries via:
```
pip3 install -r requirements.txt
```
and then run the script via:
```
python3 app.py
```

After running the app for the first time you will be asked to provide your database credentials. After first run the credentials are saved in configprod.txt.
# USAGE

Available functions:

  - `rate_restaurant(restaurant_id, bill_value, taste, size, service)`
  - `get_rating_history(restaurant_id)`
  - `get_rating(restaurant_id)`
  - `add_restaurant(restaurant_name)`

Run the tests by using:

```
pytest test_unit.py -s
```