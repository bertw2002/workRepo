# AlbertWan
# SoftDev2 pd9
# K18: Come Up For Air
# 2020-04-20

from flask import Flask, render_template
import read_csv
app = Flask(__name__)
@app.route("/")
def home():
    return render_template("index.html", data = read_csv.read_csv());

if __name__ == "__main__":
    app.debug = True
    app.run()
