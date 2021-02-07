from flask import Flask, jsonify
from calculator import PrefixCalculator, InfixCalculator

app = Flask(__name__)

@app.route("/", methods=["GET"])
def base():
    to_return = "Welcome to web-based calculator. Template for running \
                calculator queries is http://localhost:5000/calculator/calcType/expr., \
                where calcType is either prefix/infix and expr is expression for \
                evaluation. (NOTE - cannot use / in url, so substitute _ for division \
                operation)"
    return to_return

@app.route("/calculator/<string:calculator>/<string:expression>", methods=["GET"])
def get_result(expression, calculator):
    expression = expression.replace('_', '/')
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
