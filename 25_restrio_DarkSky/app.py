# Albert Wan, Tammy Chen
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
    return render_template("index.html", wind = data['consolidated_weather'][0])

@app.route("/omdb")
def omdb():
    url = "http://www.omdbapi.com/?i=tt3896198&apikey=58ce8363"
    response = request.urlopen(url)
    response = response.read()
    data = json.loads(response)
    return render_template("omdb.html",title=data['Title'],year=data['Year'],plot=data['Plot'])

@app.route("/tacos")
def second():
    u = urllib2.urlopen("http://taco-randomizer.herokuapp.com/random/")
    response = u.read()
    data = json.loads(response)
    return render_template("index1.html", cond = data['condiment'])

if __name__ == "__main__":
    app.debug = True
    app.run()
