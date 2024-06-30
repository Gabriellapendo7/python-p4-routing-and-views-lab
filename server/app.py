from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_param(parameter):
    print(parameter)
    return parameter

@app.route('/count/<int:parameter>')
def count(parameter):
     return '\n'.join(str(i) for i in range(parameter)) + '\n'

@app.route('/math/<int:a>/<operation>/<int:b>')
def math(a, operation ,b):
    if operation == '+':
        return str(a + b)
    elif operation == '-':
        return str(a - b)
    elif operation == '*':
        return str(a * b)
    elif operation == 'div':
        return str(a / b)
    elif operation == '%':
        return str(a % b)
    else:
        return 'Invalid operation'

   
if __name__ == '__main__':
    app.run(debug=True)
