from curses import keyname
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

user_dict = {"user1" : "password1", "user2" : "password2", }

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/login")
def login():
    # print(request.form["username"])
    return render_template('login.html')

@app.route("/login", methods=['GET', 'POST'])
def login_method():
    
    username = request.form["username"]
    password = request.form["password"]
    print(request.form["username"])
    print(request.form["password"])
    print(request.form)
    

    if username in user_dict:
        if password == user_dict[username]:            
            return redirect("/homepage") 
        else:
            return "<p>ERROR: Invaild login credentials</p>"
    else:
        return redirect("/signin")


@app.route("/homepage")
def homepage():
    return "<p>Login successful</p>"

@app.route("/signin")
def signin():
    return render_template('signin.html')

@app.route("/signin", methods=['GET', 'POST'])
def signin_method():
    
    print("this is signin details",request.form)

    username = request.form["username"]
    password = request.form["password"]
    if username in user_dict:
        return "<p>User already exist, please choose different</p>"
    else:
        user_dict[username] = password
        print("user dict", user_dict)
        return "<p>signin successful or signin failed</p>"



