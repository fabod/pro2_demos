from flask import Flask
from flask import render_template
import json

app = Flask("jinja")


def sachen_laden():
    with open("sachen.json") as open_file:
        sachen = json.load(open_file)
    return sachen


@app.route("/")
def jinja():

    sachen = sachen_laden()
    return render_template("index.html", dinger=sachen, zahl=3)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
