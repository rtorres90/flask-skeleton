
from mako.lookup import TemplateLookup

from app import app

lookup = TemplateLookup('./templates')

@app.route('/')
def home():
    return lookup.get_template("index.html").render(message="Hello world")

@app.route('/hello/<hello_message>')
def say_hello(hello_message):
    return lookup.get_template("hello.html").render(message=hello_message)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
