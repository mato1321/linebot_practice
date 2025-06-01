from flask import request

@app.route('/greet/<name>')
def greet(name):
    return f'Hello, {name}!'