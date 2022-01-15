from curses import keyname


user_dict = {"user1" : "password1", "user2" : "password2"}
username = "user1"
password = "password2"

if username in user_dict:
    print(user_dict[username])
    if password == user_dict[username]:
        print("yes")
    else:
        print("no")