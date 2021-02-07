# Prefix & Infix Calculator

Take Home Challenge for Machine Learning Engineer Position.

## How start up calculator
Python Version: Python 3.6.9
- `git clone https://github.com/YoannaP/take_home_exercise_kt.git`
- `cd take_home_exercise_kt`
- `pip3 install -r requirements.txt`
- `python3 main.py`
- Go to `localhost:5000/` for base page

NOTE: cannot use division sign `/` in url to query calculator so use _ instead for division as in examples below. 

## How to query calculator
Infix Examples:
- `http://localhost:5000/calculator/infix/( 1 + ( 2 * 3 ) )`
- `http://localhost:5000/calculator/infix/( ( ( 4 _ 2 ) * 4 ) + 3 )`

Prefix Examples:
- `http://localhost:5000/calculator/prefix/- _ 10 + 1 1 * 1 2`
- `http://localhost:5000/calculator/prefix/+ * 1 2 3`
