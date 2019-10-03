# Winston Peng & Albert Wan -- Team Dental Hygeine
# SoftDev1 pd9
# K15 -- Do I Know You? -- Using Cookies, Login Page
# 10-2-2019
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

user = {}

@app.route("/")
def root():
#    username = request.args['username']
#    password = request.args['password']
#    if request.cookies.get['login']:  # replace with actual conditional
#        redirect('/account')
    if False:  # change so that this will only be true if user is already logged in
        return redirect('/account')
    return redirect('/login')

@app.route('/login')
def login:
    return render_template(
        "page.html",
    )


logins = {'bertw2002': 'oreo'}


@app.route("/auth")
def route():
    """this is a temporary page that checks if login was correct"""
    username = request.args['username']
    password = request.args['password']
    print(request.cookies)
    print('decoy')
    if username not in logins.keys():
        return redirect('/username_error')
    if logins[username] != password:
        return redirect('/password_error')
    return redirect('/account')

@app.route('/account')
def login():
    """prints welcome message in account page"""
    #user = request.args['username']
    return render_template(
        'account.html'
        #user=username
    )

@app.route('/username_error')
def newuser():
    """This is where people can make a new account"""
    return render_template(
        'newuser.html'
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
