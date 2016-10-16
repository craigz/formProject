from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello assface!"

# this route is used if a name is appended to the url
# ie: http://127.0.0.1:5000/craigz
@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()
