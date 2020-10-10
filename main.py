print("simple login/register")
print("by reap-codes")
print("If u like u can donate (little bit) ;) https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=WUE2M4FLH5LYL")
print("yt: https://www.youtube.com/channel/UC4QAXdGXNLtmBCWKRonNUoA?view_as=subscriber")
print("pls fill out the Form")
username = input("Username: ")
password = input("Password: ")

s1 = 0
s2 = 0
content = ("number = 1010")

if username == ("admin"):
    print("username = check")
    s1 = 1

else:
    print("username = false")
    s1 = 0

if password == ("123psswd"):
    print("password = check")
    s2 = 1

else:
    print("password = false")
    s2 = 0

if s1 == 1 and s2 == 1:
    print("")
    print("welcome " + username)
    print(content) #<-- content here
    action = input("input: ")

else:
    print("pls log in correctly")

if action == ("change.content"):
    content = input("Type new content: ")
    print("")
    print("welcome " + username)
    print(content) #<-- content here
    action = input("input: ")

elif action == ("logout"):
    print("")
    print("pls fill out the Form")
    username = input("Username: ")
    password = input("Password: ")

else:
    print("What?")

