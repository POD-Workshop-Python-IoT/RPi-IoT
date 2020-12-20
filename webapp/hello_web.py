#!flask/bin/python
from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def helloworld():
#     return 'Hello world!'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/pod')
def pod():
    return 'Welcome to POD'

@app.route('/workshop')
def workshop():
    return render_template('workshop.html')

@app.route('/workshop/iot')
def iot():
    return render_template('workshop/new_page.html')

@app.route('/<page_name>')
def hello(page_name):
    return render_template('page.html', name=page_name)
    
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')