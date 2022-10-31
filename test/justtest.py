import random

def random_port(lower_end, upper_end):
    print(random.randint(lower_end,upper_end))
#
# random_port(100)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)
print(fact(4))