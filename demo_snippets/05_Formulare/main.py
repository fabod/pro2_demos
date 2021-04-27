from flask import Flask
from flask import render_template
from flask import request

app = Flask("templates")


@app.route("/hello/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        ziel_person = request.form['vorname']
        rueckgabe_string = "<li> " + ziel_person + "</li>"

        return render_template("begruessung.html", ansprechperson=rueckgabe_string)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
