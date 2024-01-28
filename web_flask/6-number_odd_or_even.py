#!/usr/bin/python3
"""starts a flask web application listening on 0.0.0.0:5000
"""

from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Return 'Hello HBNB' string"""
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return 'HBNB' string"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def cText(text):
    """display C followed by input text"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pythonText(text='is cool'):
    """display Python followed by input text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def isInteger(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def tempIfInteger(n):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def oddOrEven(n=None):
    """display a HTML page only if n is an integer:
    H1 tag: 'Number: n is even or odd'
    """
    if isinstance(n, int):
        if n % 2:
            res = "odd"
        else:
            res = "even"
        return render_template("6-number_odd_or_even.html", n=n, res=res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
