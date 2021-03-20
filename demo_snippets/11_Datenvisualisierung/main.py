from flask import Flask
from flask import render_template

import plotly.express as px
from plotly.offline import plot

app = Flask("Datenvisualisierung")


def get_data():
    jahr = [2015, 2016, 2017, 2018, 2019, 2021]
    loc = [1500, 3500, 12000, 9000, 10000, 4000]
    return jahr, loc


def viz():
    jahr, loc = get_data()
    fig = px.bar(x=jahr, y=loc)
    div = plot(fig, output_type="div")
    return div


@app.route("/")
def index():
    div = viz()
    return render_template('index.html', name="Fabian", viz_div=div)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
