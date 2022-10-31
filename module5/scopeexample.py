# global scope
txt = "The greatest class ever!"
counter = 0
def add_a_student():
    # local scope
    # txt = "The best class ever!"
    global txt # avoid this as much as possible
    print(txt)
    txt = "We are in a great class"

func()
print(txt)
