# Albert Wan
# SoftDev1 pd09
# K #25: Getting More REST
# 2019-11-13

from flask import Flask, render_template
import urllib.request as urllib2
import json
app = Flask(__name__)

@app.route("/")
def root():
    u = urllib2.urlopen("https://www.metaweather.com/api/location/44418/")
    response = u.read()
    data = json.loads(response)
    return render_template("index.html", wind = data['consolidated_weather'])

if __name__ == "__main__":
    app.debug = True
    app.run()
