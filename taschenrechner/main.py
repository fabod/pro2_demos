from flask import Flask
from flask import render_template
from flask import request

app = Flask("taschenrechner")


@app.route("/", methods=['GET', 'POST'])
def rechner():
    if request.method == 'POST':
        zahl_1 = request.form['zahl_1']
        zahl_2 = request.form['zahl_2']
        zahl_3 = request.form['zahl_3']
        summe = int(zahl_1) + int(zahl_2) + int(zahl_3)
        antwort = "Die Summe der Zahlen ist: " + str(summe)
        return antwort

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
