from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", title="Home", description="hello")


if __name__ == '__main__':
    my_host = "127.0.0.1"
    app.run(host=my_host, debug=True)