from flask import Flask, request, jsonify, abort

app = Flask(__name__)
app.run(debug=True)


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
    sum = (num1 / num2)
    return str(sum), 200


# Part 2 of task
@app.route('/calc/web/sum?number=<int:number>&number=<int:number>/')
def calc_sum(number):
    if not request.json:
        abort(400)
    try:
        params = request.args.to_dict(flat=False)
        p = params['number']
        total = 0
        for total_number in p:
            total = total + total_number
        return str(total), 200
    except KeyError:
        abort(400)


@app.route('/calc/web/mean?number=<int:number>&number=<int:number>/')
def calc_sum(number):
    if not request.json:
        abort(400)
    try:
        params = request.args.to_dict(flat=False)
        p = params['number']
        total = 0
        for total_number in p:
            total = (total * total_number) / p
        return str(total), 200
    except KeyError:
        abort(400)
