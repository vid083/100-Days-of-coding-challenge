from flask import Flask, render_template, request, redirect

app = Flask(__name__)

user_dict = {"user1" : "password1", "user2" : "password2"}

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login")
def login():
    # print(request.form["username"])
    return render_template('login.html')

@app.route("/login", methods=['GET', 'POST'])
def login_method():
    '''
    Check whether user exist or not
    if user not exist redirect to signin route
    if user exist check password corret or not 
    if password correct redirect to homeoage
    if password not correct display error message in login page
    '''
    print(request.form["username"])
    print(request.form["password"])
    print(request.form)
    return redirect("/homepage")

@app.route("/homepage")
def homepage():
    return "<p>html</p>"

