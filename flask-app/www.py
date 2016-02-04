import logging
from logging.handlers import RotatingFileHandler

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
    formatter = logging.Formatter("[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s")
    handler = RotatingFileHandler('/var/log/flask.log', maxBytes=10000000, backupCount=1)
    handler.setLevel(logging.DEBUG)
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)
    app.run(debug=False, host='0.0.0.0', port=80)
