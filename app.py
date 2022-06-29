from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Welcome to the SQEPtech Calculator"


@app.route('/calc/')
def calc_page():
    return "You've reached the 2nd endpoint, /calc/"


@app.route('/calc/web/')
def calc_web_page():
    return "You've reached here"

# Part 1 of task


@app.route('/calc/web/add/<int:num1>/to/<int:num2>/')
def calc_addition(num1, num2):
    sum = num1 + num2
    return str(sum), 200


@app.route('/calc/web/subtract/<int:num1>/from/<int:num2>/')
def calc_subtraction(num1, num2):
    sum = num1 - num2
    return str(sum), 200


@app.route('/calc/web/multiply/<int:num1>/by/<int:num2>/')
def calc_multiply(num1, num2):
    sum = num1 * num2
    return str(sum), 200


@app.route('/calc/web/divide/<int:num1>/by/<int:num2>/')
def calc_divide(num1, num2):
    sum = num1 / num2
    return str(sum), 200


# Part 2 of task
@app.route('/calc/web/sum?number=<int:num>&number=<int:num>/')
def calc_sum(arg1, arg2):
    sum(n1+n2)
    return str(sum), 200
