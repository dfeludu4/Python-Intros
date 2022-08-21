x = "awesome"

def myfunc():
    global x
    x = "fabolous"
    print("Python is " + x)

myfunc()

print("Python is " + x)
