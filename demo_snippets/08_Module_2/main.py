from flask import Flask
import preise
import gutscheine
app = Flask("module")


@app.route("/rabatt/<preis>")
def rabatt(preis):
    preis_mit_rabatt = preise.rabatt(preis)

    return "Der neue Preis ist: " + str(preis_mit_rabatt)


@app.route("/gutschein/<preis>/<gutschein>")
def gutschein(preis, gutschein):
    gutscheine = "sdfkj"
    preis_mit_rabatt = gutscheine.rabatt(preis, gutschein)

    return "Der neue Preis mit Gutschein ist: " + str(preis_mit_rabatt)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
