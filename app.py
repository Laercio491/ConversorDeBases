
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/integrantes")
def integrantes():
    return render_template("integrantes.html")


@app.route("/conversor")
def conversor():
    return render_template("conversor.html")


if __name__ == "__main__":
    app.run(debug=True)
