from flask import Flask


app = Flask(__name__)


@app.route('/')
def index():
    return "Hi"


if __name__ == '__main__':
    my_host = "127.0.0.1"
    app.run(host=my_host, debug=True)