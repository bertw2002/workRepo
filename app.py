from flask import Flask, render_template
import random
app = Flask(__name__)

@app.route("/")
def route():
    print(app)
    return ""

if __name__ == "__main__":
    app.debug = True
    app.run()
