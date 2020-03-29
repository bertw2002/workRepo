#Albert Wan pd9

from flask import Flask
from flask import render_template


app = Flask(__name__)
@app.route("/")
def root():
    return render_template("page0.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
