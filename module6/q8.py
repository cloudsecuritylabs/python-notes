x = 10
def func():
    #local scope
    global x
    x = 20
    # print(x)
    # return x
func()
print(x)