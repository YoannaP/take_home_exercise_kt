from flask import Flask, jsonify
from calculator import PrefixCalculator, InfixCalculator

app = Flask(__name__)

@app.route("/calculator/<string:calculator>/<string:expression>", methods=["GET"])
def get_book(expression, calculator):
    if calculator=='infix':
        calc = InfixCalculator()
    elif calculator=='prefix':
        calc = PrefixCalculator()

    result = calc.evaluate(expression)

    # return it as a string
    to_return = "Result of " + calculator + " calculator is " + str(result)
    return to_return

if __name__ == "__main__":
    app.run()
