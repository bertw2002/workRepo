# Albert Wan
# SoftDev1 pd09
# K24 -- A RESTful Journey Skyward
# 2019-11-12

from flask import Flask, render_template
import urllib.request as urllib2
import json
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=1mctX2wSTadgHMZMp0no7IgATAIs37Ita7kYpowF")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", pic = data['url'])

if __name__ == "__main__":
    app.debug = True
    app.run()
