#Albert Wan
#SoftDev1 pd9
#K08 -- Lemme Flask You Sump’n
#2019-09-19

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
print(__name__)
return "no hablo queso!"

@app.route("/")
def bestFood():
print(__name__)
return "I like pizza"

@app.route("/")
def OSXorWindows():
print(__name__)
return "OSX"

if __name__ == "__main__":
app.debug = True
app.run()
