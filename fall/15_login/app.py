# Winston Peng & Albert Wan -- Team Dental Hygeine
# SoftDev1 pd9
# K15 -- Do I Know You? -- Using Cookies, Login Page
# 10-2-2019
from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "unique key no one knows about"

@app.route("/")
def root():
    #checks if you are logged in from same session to prevent errors
    if "loggedin" in session:
        return render_template('account.html')
    # else, just go to regular login page
    return redirect('/login')

@app.route('/login')
def login():
    #checks if you are logged in from same session to prevent errors
    if "loggedin" in session:
        return render_template('account.html')
        #else, just go to regular login page.
    return render_template(
        "page.html",
    )

usern = "bert"
pas = "oreo"


@app.route("/auth")
def route():
    """this is a temporary page that checks if login was correct"""
    if (usern == request.args['username']):
        if (pas == request.args['password']):
            session["loggedin"] = True
            # if you put in the correct user and password,
            # make the logging for session true.
    if usern != request.args['username']:
        return redirect('/username_error')
        # if username wrong, go to username error path, vice versa
    if pas != request.args['password']:
        return redirect('/password_error')
    return redirect('/login')


@app.route('/logout')
def logout():
    if "loggedin" in session:
        #erase loggedin
        session.pop("loggedin")
    #if log out, go back to login page
    return render_template('page.html')

@app.route('/username_error')
def usererror():
    #This is where people can make a new account"""
    return render_template(
        'usererror.html'
    )

@app.route('/password_error')
def passerror():
    #This is where people can make a new account"""
    return render_template(
        'passerror.html'
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
