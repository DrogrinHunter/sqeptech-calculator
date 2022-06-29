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

@app.route('/calc/web/add/<int:num1>/to/<int:num2>/')
def calc_addition(num1, num2):
    sum = num1 + num2
    return str(sum), 200


