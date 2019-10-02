from flask import Flask, render_template, request, redirect
import random
app = Flask(__name__)

@app.route("/")
def occupy():
    print("hello")
    return render_template("page.html")

@app.route("/auth")
def route():
    return render_template

if __name__ == "__main__":
    app.debug = True
    app.run()
