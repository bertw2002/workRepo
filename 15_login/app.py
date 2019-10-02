from flask import Flask, render_template, request, redirect, url_for
import random
app = Flask(__name__)

@app.route("/")
def occupy():
    print("hello")
    return render_template(
        "page.html",
        username = request.args['username'],
        password = request.args['password']
        )

logins = {'bertw2002':'oreo'}

@app.route("/auth")
def route():
    if logins[username] == password:
        return redirect("https://xkcd.com") # replace with login page
    if not username in logins.keys():
        return redirect('blah') # replace with create account page

if __name__ == "__main__":
    app.debug = True
    app.run()
