# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, Google!'


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form.get('name', 'Guest')
    return render_template('greet.html', name=name)
